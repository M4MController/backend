import proto.objects_pb2_grpc as objects_pb2_grpc
import proto.objects_pb2 as objects_pb2
from google.protobuf.json_format import MessageToJson
from concurrent import futures
from collections import defaultdict
import grpc
import time
import config
import logging
import psycopg2

class ObjectServiceServ(objects_pb2_grpc.ObjectServiceServicer):
    def __init__(self, model):
        self.__model = model

    #     OBJECTS.ID, OBJECT.NAME, OBJECT.USER_ID, OBJECT.ADRES,
    # CONTROLLERS.ID, CONTROLLERS.NAME, CONTROLLERS.OBJECT_ID,
    # CONTROLLERS.META, CONTROLLERS.ACTIVATION_DATE, CONTROLLERS.STATUS,
    # CONTROLLERS.MAC,  CONTROLLERS.DEACTIVATION_DATE,  CONTROLLERS.CONTROLLER_TYPE,
    # SENSOR.ID, SENSOR.NAME, SENSOR.CONTROLLER_ID, SENSOR.ACTIVATION_DATE, 
    # SENSOR.STATUS, SENSOR.DEACTIVATION_DATE, SENSOR.SENSOR_TYPE, SENSOR.COMPANY,


# id name user_id adres
# id name object_id meta activation_date status mac deactivation_date controller_type
# id name controller_id activation_date status deactivation_date sensor_type company 
# 0    1            2         3
# 1, 'Имя Объекта', 1, 'Улица Пушкина, Дом Колотушкина'
# 4          5          6       7                               8                       9     10                  11  12
# 1, 'test_controller', 1, 'Улица Пушкина, Дом Колотушкина', datetime.date(2001, 1, 1), 1, '6b:45:cd:97:48:48', None, 1
# 13   14          15  16                         17 18    19 20
# 1, 'test_sensor', 1, datetime.date(2001, 1, 1), 1, None, 1, 'GASPROM'

    def GetUsersInfo(self, request, context):
        logging.info("starting to process")
        cur = self.__model.cursor()
        user_id = request.user_id
        logging.info("Executing query")
        cur.execute("""SELECT * FROM OBJECTS INNER JOIN CONTROLLERS ON CONTROLLERS.object_id = OBJECTS.id INNER JOIN SENSOR ON SENSOR.controller_id = CONTROLLERS.id
            WHERE user_id = %s ;""",(user_id,))
        rows = cur.fetchall()
        logging.info("Executed query")
        uinf = objects_pb2.UserInfoH(
            id=user_id,
            objects=[],
        )
        controllers = {}
        controllers_l = defaultdict(list)
        sensors = {}
        objects = {}
        objects_l = defaultdict(list)
        for i in rows:
            logging.debug("loaded: {}".format(i))
            if i[0] not in objects:
                objects[i[0]] = objects_pb2.ObjectInfo(
                    id=i[0],
                    name=i[1],
                    user_id=i[2],
                    adres=i[3],
                    controllers=[]
                )
            obct = objects[i[0]]
            if not i[0] in uinf.objects:
                logging.debug("object found")

            if i[4] not in controllers:
                ctrl = objects_pb2.ControllerInfo(
                    id=i[4],
                    name=i[5],
                    object_id=i[6],
                    meta=i[7],
                    activation_date=int(time.mktime(i[8].timetuple())),
                    status=i[9],
                    mac=i[10],
                    controller_type=i[12],
                    sensors=[]
                )
                if i[11] is None:
                    ctrl.deactivation_date_null = True
                else:
                    ctrl.deactivation_date_val = int(time.mktime(i[11].timetuple()))
                controllers[i[4]] = ctrl
            ctrl = controllers[i[4]]
            if not ctrl in objects_l[i[0]]:
                logging.debug("controller found")
                objects_l[i[0]].append(ctrl)

            if i[13] not in sensors:
                ssr = objects_pb2.SensorInfo(
                    id=i[13],
                    name=i[14],
                    controller_id=i[15],
                    activation_date=int(time.mktime(i[16].timetuple())),
                    status=i[17],
                    sensor_type=i[19],
                    company=i[20]
                )
                if i[18] is None:
                    ssr.deactivation_date_null = True
                else:
                    ssr.deactivation_date_val = int(time.mktime(i[18].timetuple())),
                sensors[i[13]] = ssr
            snsor = sensors[i[13]]
            if not snsor in controllers_l[i[4]]:
                logging.debug("sensor found")
                controllers_l[i[4]].append(snsor)
        
        for ctr, vals in controllers_l.items():
            controllers[ctr].sensors.extend(vals)

        for ob, vals in objects_l.items():
            objects[ob].controllers.extend(vals)

        uinf.objects.extend(objects.values())

        logging.debug("ending")
        logging.debug(MessageToJson(uinf))
        return uinf
    
    def GetControllerInfo(self, request, context):
        logging.info("starting to process")
        cur = self.__model.cursor()
        controller_id = request.controller_id
        logging.info("Executing query")
        cur.execute("""SELECT * FROM CONTROLLERS INNER JOIN SENSOR ON SENSOR.controller_id = CONTROLLERS.id
            WHERE CONTROLLERS.id = %s ;""",(controller_id,))
        rows = cur.fetchall()
        logging.info("Executed query")
        i = rows[0]
        ctrl = objects_pb2.ControllerInfo(
                    id=i[0],
                    name=i[1],
                    object_id=i[2],
                    meta=i[3],
                    activation_date=int(time.mktime(i[4].timetuple())),
                    status=i[5],
                    mac=i[6],
                    controller_type=i[8],
                    sensors=[]
                )
        if i[7] is None:
            ctrl.deactivation_date_null = True
        else:
            ctrl.deactivation_date_val = int(time.mktime(i[11].timetuple()))
        sensors = {}
        for i in rows:
            logging.debug("loaded: {}".format(i))
            if i[9] not in sensors:
                ssr = objects_pb2.SensorInfo(
                    id=i[9],
                    name=i[10],
                    controller_id=i[11],
                    activation_date=int(time.mktime(i[12].timetuple())),
                    status=i[13],
                    sensor_type=i[15],
                    company=i[16]
                )
                if i[14] is None:
                    ssr.deactivation_date_null = True
                else:
                    ssr.deactivation_date_val = int(time.mktime(i[14].timetuple())),
                sensors[i[13]] = ssr
            snsor = sensors[i[13]]
            ctrl.sensors.extend([snsor,])
        logging.debug("ending")
        logging.debug(MessageToJson(ctrl))
        return ctrl

    def GetSensorInfo(self, request, context):
        logging.info("starting to process")
        cur = self.__model.cursor()
        sensor_id = request.sensor_id
        logging.info("Executing query")
        cur.execute("""SELECT * FROM SENSOR 
            WHERE SENSOR.id = %s ;""",(sensor_id,))
        rows = cur.fetchall()
        logging.info("Executed query")
        i = rows[0]
        sns = objects_pb2.SensorInfo(
                    id=i[0],
                    name=i[1],
                    controller_id=i[2],
                    activation_date=int(time.mktime(i[3].timetuple())),
                    status=i[4],
                    sensor_type=i[6],
                    company=i[7]
                )
        if i[9] is None:
            sns.deactivation_date_null = True
        else:
            sns.deactivation_date_val = int(time.mktime(i[9].timetuple()))
        logging.debug("ending")
        logging.debug(MessageToJson(sns))
        return sns

    def GetObjectInfo(self, request, context):
        logging.info("starting to process")
        cur = self.__model.cursor()
        oid = request.object_id
        logging.info("Executing query")
        cur.execute("""SELECT * FROM OBJECTS INNER JOIN CONTROLLERS ON CONTROLLERS.object_id = OBJECTS.id INNER JOIN SENSOR ON SENSOR.controller_id = CONTROLLERS.id
            WHERE OBJECTS.id = %s ;""",(oid,))
        rows = cur.fetchall()
        logging.info("Executed query")
        controllers = {}
        controllers_l = defaultdict(list)
        sensors = {}
        objects = {}
        objects_l = defaultdict(list)
        for i in rows:
            logging.debug("loaded: {}".format(i))
            if i[0] not in objects:
                objects[i[0]] = objects_pb2.ObjectInfo(
                    id=i[0],
                    name=i[1],
                    user_id=i[2],
                    adres=i[3],
                    controllers=[]
                )
            obct = objects[i[0]]

            if i[4] not in controllers:
                ctrl = objects_pb2.ControllerInfo(
                    id=i[4],
                    name=i[5],
                    object_id=i[6],
                    meta=i[7],
                    activation_date=int(time.mktime(i[8].timetuple())),
                    status=i[9],
                    mac=i[10],
                    controller_type=i[12],
                    sensors=[]
                )
                if i[11] is None:
                    ctrl.deactivation_date_null = True
                else:
                    ctrl.deactivation_date_val = int(time.mktime(i[11].timetuple()))
                controllers[i[4]] = ctrl
            ctrl = controllers[i[4]]
            if not ctrl in objects_l[i[0]]:
                logging.debug("controller found")
                objects_l[i[0]].append(ctrl)

            if i[13] not in sensors:
                ssr = objects_pb2.SensorInfo(
                    id=i[13],
                    name=i[14],
                    controller_id=i[15],
                    activation_date=int(time.mktime(i[16].timetuple())),
                    status=i[17],
                    sensor_type=i[19],
                    company=i[20]
                )
                if i[18] is None:
                    ssr.deactivation_date_null = True
                else:
                    ssr.deactivation_date_val = int(time.mktime(i[18].timetuple())),
                sensors[i[13]] = ssr
            snsor = sensors[i[13]]
            if not snsor in controllers_l[i[4]]:
                logging.debug("sensor found")
                controllers_l[i[4]].append(snsor)
        
        for ctr, vals in controllers_l.items():
            controllers[ctr].sensors.extend(vals)

        for ob, vals in objects_l.items():
            objects[ob].controllers.extend(vals)
        uinf = list(objects.values())[0]
        logging.debug("ending")
        logging.debug(MessageToJson(uinf))
        return uinf

        
def main():
    confs = config.ConfigManager()
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    addres = confs["addres"]
    logging.info("Starting grpc server with addres :{}".format(addres))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    dbconf = confs["database"]
    database = psycopg2.connect(dbname=dbconf["database"], 
                                user=dbconf["username"], 
                                password=dbconf["password"],
                                host=dbconf["url"])
    objects_pb2_grpc.add_ObjectServiceServicer_to_server(ObjectServiceServ(database), server)
    server.add_insecure_port(addres)
    server.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Stop signal got")
        server.stop(0)

if __name__ == '__main__':
    main()