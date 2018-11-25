import proto.objects_pb2_grpc as objects_pb2_grpc
import proto.objects_pb2 as objects_pb2
import proto.utils_pb2 as utils_pb2
from google.protobuf.json_format import MessageToJson
from concurrent import futures
from collections import defaultdict
import grpc
import time
import config
import logging
import psycopg2
import argparse

class ObjectServiceServ(objects_pb2_grpc.ObjectServiceServicer):
    def __init__(self, model):
        self.__model = model

    #     OBJECTS.ID, OBJECT.NAME, OBJECT.USER_ID, OBJECT.address,
    # CONTROLLERS.ID, CONTROLLERS.NAME, CONTROLLERS.OBJECT_ID,
    # CONTROLLERS.META, CONTROLLERS.ACTIVATION_DATE, CONTROLLERS.STATUS,
    # CONTROLLERS.MAC,  CONTROLLERS.DEACTIVATION_DATE,  CONTROLLERS.CONTROLLER_TYPE,
    # SENSOR.ID, SENSOR.NAME, SENSOR.CONTROLLER_ID, SENSOR.ACTIVATION_DATE, 
    # SENSOR.STATUS, SENSOR.DEACTIVATION_DATE, SENSOR.SENSOR_TYPE, SENSOR.COMPANY,


# id name user_id address
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
        logging.info("Executing query user id = {}".format(user_id))
        cur.execute("""SELECT * FROM OBJECTS LEFT JOIN CONTROLLERS ON CONTROLLERS.object_id = OBJECTS.id LEFT JOIN SENSOR ON SENSOR.controller_id = CONTROLLERS.id
            WHERE user_id = %s ;""",(user_id,))
        rows = cur.fetchall()
        logging.info("Executed query")
        logging.info(rows)
        uinf = objects_pb2.UserInfoH(
            id=utils_pb2.UserId(
                user_id=int(user_id),
            ),
            objects=[],
        )
        controllers = {}
        controllers_l = defaultdict(list)
        sensors = {}
        objects = {}
        objects_l = defaultdict(list)
        for i in rows:
            logging.debug("loaded: {}".format(i))
            if (i[0] not in objects) and (i[0] is not None):
                objects[i[0]] = objects_pb2.ObjectInfo(
                    id=utils_pb2.ObjectId(
                        object_id=int(i[0]),
                    ),
                    name=i[1],
                    user_id=utils_pb2.UserId(
                        user_id=int(i[2]),
                    ),
                    address=i[3],
                    controllers=[]
                )
            
            if i[0] is not None:
                obct = objects[i[0]]
                if not i[0] in uinf.objects:
                    logging.debug("object found")

            if (i[4] not in controllers) and (i[4] is not None):
                ctrl = objects_pb2.ControllerInfo(
                    id=utils_pb2.ControllerId(
                        controller_id=int(i[4]),
                    ),
                    name=i[5],
                    object_id=utils_pb2.ObjectId(
                        object_id=int(i[6]),
                    ),
                    meta=i[7],
                    status=i[9],
                    mac=i[10],
                    controller_type=i[12],
                    sensors=[]
                )
                if i[8] is None:
                    ctrl.activation_date_null = True
                else:
                    ctrl.activation_date_val = int(time.mktime(i[8].timetuple()))
                if i[11] is None:
                    ctrl.deactivation_date_null = True
                else:
                    ctrl.deactivation_date_val = int(time.mktime(i[11].timetuple()))
                controllers[i[4]] = ctrl
            if (i[4] is not None) and (i[0] is not None):
                ctrl = controllers[i[4]]
                if not ctrl in objects_l[i[0]]:
                    logging.debug("controller found")
                    objects_l[i[0]].append(ctrl)

            if (i[13] not in sensors) and (i[13] is not None):
                ssr = objects_pb2.SensorInfo(
                    id=utils_pb2.SensorId(
                        sensor_id=int(i[13]),
                    ),
                    name=i[14],
                    controller_id=utils_pb2.ControllerId(
                        controller_id=int(i[15]),
                    ),
                    status=i[17],
                    sensor_type=i[19],
                    company=i[20]
                )
                if i[16] is None:
                    ssr.activation_date_null = True
                else:
                    ssr.activation_date_val = int(time.mktime(i[16].timetuple()))
                if i[18] is None:
                    ssr.deactivation_date_null = True
                else:
                    ssr.deactivation_date_val = int(time.mktime(i[18].timetuple())),
                sensors[i[13]] = ssr
            
            if (i[13] is not None) and (i[4] is not None):
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
    
    def _get_controller_info(self, controller_id):
        cur = self.__model.cursor()
        logging.info("Executing query")
        cur.execute("""SELECT * FROM CONTROLLERS LEFT JOIN SENSOR ON SENSOR.controller_id = CONTROLLERS.id
            WHERE CONTROLLERS.id = %s ;""", (controller_id,))
        rows = cur.fetchall()
        logging.info("Executed query")
        i = rows[0]
        object_id = None 
        if i[2] is not None:
            object_id = utils_pb2.ObjectId(
                        object_id=int(i[2]),
                    )
        ctrl = objects_pb2.ControllerInfo(
                    id=utils_pb2.ControllerId(
                        controller_id=int(i[0]),
                    ),
                    name=i[1],
                    object_id=object_id,
                    meta=i[3],
                    status=i[5],
                    mac=i[6],
                    controller_type=i[8],
                    sensors=[])
        if i[4] is None:
            ctrl.activation_date_null = True
        else:
            ctrl.activation_date_val = int(time.mktime(i[4].timetuple()))
        
        if i[7] is None:
            ctrl.deactivation_date_null = True
        else:
            ctrl.deactivation_date_val = int(time.mktime(i[11]))
        sensors = {}
        snsor = None
        for i in rows:
            logging.debug("loaded: {}".format(i))
            if (i[9] not in sensors) and (i[9] is not None):
                ssr = objects_pb2.SensorInfo(
                    id=utils_pb2.SensorId(
                        sensor_id=int(i[9]),
                    ),
                    name=i[10],
                    controller_id=utils_pb2.ControllerId(
                        controller_id=int(i[11]),
                    ),
                    status=i[13],
                    sensor_type=i[15],
                    company=i[16]
                )
                if i[12] is None:
                    ssr.activation_date_null = True
                else:
                    ssr.activation_date_val = int(time.mktime(i[12].timetuple()))
                if i[14] is None:
                    ssr.deactivation_date_null = True
                else:
                    ssr.deactivation_date_val = int(time.mktime(i[14].timetuple()))
                sensors[i[13]] = ssr
            if i[13] is not None:
                snsor = sensors[i[13]]
            if snsor is not None:
                ctrl.sensors.extend([snsor,])
        return ctrl

    def GetControllerInfo(self, request, context):
        logging.info("starting to process")
        controller_id = request.controller_id
        ctrl = self._get_controller_info(controller_id)
        logging.debug("ending")
        logging.debug(MessageToJson(ctrl))
        return ctrl

    def _get_sensor_info(self, sensor_id):
        cur = self.__model.cursor()
        logging.info("Executing query")
        cur.execute("""SELECT * FROM SENSOR 
            WHERE SENSOR.id = %s ;""",(sensor_id,))
        rows = cur.fetchall()
        logging.info("Executed query")
        i = rows[0]
        sns = objects_pb2.SensorInfo(
                    id=utils_pb2.SensorId(
                        sensor_id=int(i[0]),
                    ),
                    name=i[1],
                    controller_id=utils_pb2.ControllerId(
                        controller_id=int(i[2]),
                    ),
                    status=i[4],
                    sensor_type=i[6],
                    company=i[7],)
        if i[3] is None:
            sns.activation_date_null = True
        else:
            sns.activation_date_val = int(time.mktime(i[3].timetuple()))
        
        if i[5] is None:
            sns.deactivation_date_null = True
        else:
            sns.deactivation_date_val = int(time.mktime(i[5].timetuple()))
        return sns

    def GetSensorInfo(self, request, context):
        logging.info("starting to process")
        sensor_id = request.sensor_id
        sns = self._get_sensor_info(sensor_id)
        logging.debug("ending")
        logging.debug(MessageToJson(sns))
        return sns

    def _get_object_info(self, oid):
        cur = self.__model.cursor()
        logging.info("Executing query")
        cur.execute("""SELECT * FROM OBJECTS LEFT JOIN CONTROLLERS ON CONTROLLERS.object_id = OBJECTS.id LEFT JOIN SENSOR ON SENSOR.controller_id = CONTROLLERS.id
            WHERE OBJECTS.id = %s ;""", (oid,))
        rows = cur.fetchall()
        logging.info("Executed query:")
        logging.info(rows)
        controllers = {}
        controllers_l = defaultdict(list)
        sensors = {}
        objects = {}
        objects_l = defaultdict(list)
        for i in rows:
            logging.debug("loaded: {}".format(i))
            if (i[0] not in objects) and (i[0] is not None):
                objects[i[0]] = objects_pb2.ObjectInfo(
                    id=utils_pb2.ObjectId(
                        object_id=int(i[0]),
                    ),
                    name=i[1],
                    user_id=utils_pb2.UserId(
                        user_id=int(i[2]),
                    ),
                    address=i[3],
                    controllers=[],)
            obct = objects[i[0]]

            if (i[4] not in controllers) and (i[4] is not None):
                ctrl = objects_pb2.ControllerInfo(
                    id=utils_pb2.ControllerId(
                        controller_id=int(i[4]),
                    ),
                    name=i[5],
                    object_id=utils_pb2.ObjectId(
                        object_id=int(i[6]),
                    ),
                    meta=i[7],
                    status=i[9],
                    mac=i[10],
                    controller_type=i[12],
                    sensors=[],)
                if i[8] is None:
                    ctrl.activation_date_null = True
                else:
                    ctrl.activation_date_val = int(time.mktime(i[8].timetuple()))
                if i[11] is None:
                    ctrl.deactivation_date_null = True
                else:
                    ctrl.deactivation_date_val = int(time.mktime(i[11].timetuple()))
                controllers[i[4]] = ctrl

            if (i[4] is not None) and (i[0] is not None):
                ctrl = controllers[i[4]]
                if not ctrl in objects_l[i[0]]:
                    logging.debug("controller found")
                    objects_l[i[0]].append(ctrl)

            if (i[13] not in sensors) and (i[13] is not None):
                ssr = objects_pb2.SensorInfo(
                    id=utils_pb2.SensorId(
                        sensor_id=int(i[13]),
                    ),
                    name=i[14],
                    controller_id=utils_pb2.ControllerId(
                        controller_id=int(i[15]),
                    ),
                    status=i[17],
                    sensor_type=i[19],
                    company=i[20],)
                if i[16] is None:
                    ctrl.activation_date_null = True
                else:
                    ctrl.activation_date_val = int(time.mktime(i[16].timetuple()))
                if i[18] is None:
                    ssr.deactivation_date_null = True
                else:
                    ssr.deactivation_date_val = int(time.mktime(i[18].timetuple()))
                sensors[i[13]] = ssr
            if (i[13] is not None) and (i[4] is not None):
                snsor = sensors[i[13]]
                if (not snsor in controllers_l[i[4]]):
                    logging.debug("sensor found")
                    controllers_l[i[4]].append(snsor)
        
        for ctr, vals in controllers_l.items():
            controllers[ctr].sensors.extend(vals)

        for ob, vals in objects_l.items():
            objects[ob].controllers.extend(vals)
        uinf = list(objects.values())[0]
        return uinf

    def GetObjectInfo(self, request, context):
        logging.info("starting to process")
        oid = request.object_id
        uinf = self._get_object_info(oid)
        logging.debug("ending")
        logging.debug(MessageToJson(uinf))
        return uinf

    def CreateObject(self, request, context):
        with self.__model.cursor() as cur:
            try:
                status = 0
                cur.execute("""INSERT INTO  OBJECTS VALUES (
                              default,
                              %s,
                              %s,
                              %s
                            )
                            RETURNING id;""", (
                            request.name,
                            1,
                            request.address))

                rows = cur.fetchall()
                object_id = rows[0][0]
                self.__model.commit()
                logging.info("Executed query")
            except Exception as e:
                logging.error("Failed query {}".format(str(e)))
                self.__model.rollback()
        return self._get_object_info(object_id)

    def CreateController(self, request, context):
        # request.ControllerInit
        with self.__model.cursor() as cur:
            try:
                status = 0
                cur.execute("""INSERT INTO CONTROLLERS (status, mac, controller_type) VALUES (
                              %s,
                              %s,
                              %s)
                              RETURNING id;""", (status,
                            request.mac,
                            request.controller_type))
                rows = cur.fetchall()
                controller_id = rows[0][0]
                self.__model.commit()
                logging.info("Executed query")
            except Exception as e:
                logging.error("Failed query {}".format(str(e)))
                self.__model.rollback()
        return self._get_controller_info(controller_id)

    def CreateSensor(self, request, context):
        # request.SensorInit
        with self.__model.cursor() as cur:
            status = 0
            try:
                cur.execute("""INSERT INTO SENSOR VALUES (
                    DEFAULT,
                    %s,
                    %s,
                    %s,
                    %s,
                    NULL,
                    %s,
                    %s)
                    RETURNING id; """, (request.name,
                            request.controller_id,
                            request.date,
                            status,
                            request.sensor_type,
                            request.company))
                rows = cur.fetchall()
                sensor_id = rows[0][0]
                self.__model.commit()
                logging.info("Executed query")
            except Exception as e:
                logging.error("Failed query {}".format(str(e)))
                self.__model.rollback()
        return self._get_sensor_info(sensor_id)

    def ActivateController(self, request, context):
        # request.ControllerActivate
        with self.__model.cursor() as cur:
            try:
                status = 0
                cur.execute("""
                    UPDATE CONTROLLERS SET
                      name = %s,
                      meta = %s,
                      object_id = %s,
                      status = %s,
                      activation_date = now()
                    where id = %s;
                """, (request.name, request.meta, request.object_id.object_id, status, request.id.controller_id))
                self.__model.commit()
                logging.info("Executed query")
            except Exception as e:
                logging.error("Failed query {}".format(str(e)))
                self.__model.rollback()
        return self._get_controller_info(request.id.controller_id)

    def DeleteObject(self, request, context):
        with self.__model.cursor() as cur:
            try:
                status = 0
                cur.execute("""
                    DELETE FROM OBJECTS
                    where id = %s;
                """, (request.object_id, ))
                self.__model.commit()
                logging.info("Executed query")
            except Exception as e:
                logging.error("Failed query {}".format(str(e)))
                self.__model.rollback()
        return utils_pb2.Void()
    
    def DeleteSensor(self, request, context):
        with self.__model.cursor() as cur:
            try:
                status = 0
                cur.execute("""
                    DELETE FROM SENSOR
                    where id = %s;
                """, (request.object_id, ))
                self.__model.commit()
                logging.info("Executed query")
            except Exception as e:
                logging.error("Failed query {}".format(str(e)))
                self.__model.rollback()
        return utils_pb2.Void()
    
    def DeleteController(self, request, context):
        with self.__model.cursor() as cur:
            try:
                status = 0
                cur.execute("""
                    DELETE FROM CONTROLLERS
                    where id = %s;
                """, (request.object_id, ))
                self.__model.commit()
                logging.info("Executed query")
            except Exception as e:
                logging.error("Failed query {}".format(str(e)))
                self.__model.rollback()
        return utils_pb2.Void()
    
    def DeactivateController(self, request, context):
        with self.__model.cursor() as cur:
            try:
                status = 0
                cur.execute("""
                    UPDATE CONTROLLERS SET
                      name = NULL,
                      meta = NULL,
                      object_id = NULL,
                      deactivation_date = now(),
                      status = 0
                    where id = %s;
                """, (status, request.controller_id, ))
                self.__model.commit()
                logging.info("Executed query")
            except Exception as e:
                logging.error("Failed query {}".format(str(e)))
                self.__model.rollback()
        return self._get_controller_info(request.controller_id)


def main():
    parser = argparse.ArgumentParser(description="""
        Service to store objects
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    confs = config.ConfigManager()
    if args.config is not None:
        with open(args.config, "r") as conffile:
            confs.load_from_file(conffile)
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    address = confs["address"]
    logging.info("Starting grpc server with address :{}".format(address))
    logging.info("Starting grpc server {} workers".format(confs["workers"]))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=confs["workers"]))
    dbconf = confs["database"]
    database = psycopg2.connect(dbname=dbconf["database"],
                                user=dbconf["username"],
                                password=dbconf["password"],
                                host=dbconf["host"])
    objects_pb2_grpc.add_ObjectServiceServicer_to_server(ObjectServiceServ(database), server)
    server.add_insecure_port(address)
    server.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Stop signal got")
        server.stop(0)

if __name__ == '__main__':
    main()
