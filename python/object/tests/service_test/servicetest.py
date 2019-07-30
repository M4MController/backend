import grpc
from proto import objects_pb2_grpc
from proto import objects_pb2
from proto import utils_pb2
from google.protobuf.json_format import MessageToJson
import datetime

if __name__ == "__main__":
    objs_chan = grpc.insecure_channel("127.0.0.1:6001")
    observ = objects_pb2_grpc.ObjectServiceStub(objs_chan)
    res = observ.GetUsersInfo(utils_pb2.UserId(user_id=1))
    print(MessageToJson(res))
    res = observ.GetControllerInfo(utils_pb2.ControllerId(controller_id=1))
    print(MessageToJson(res))
    res = observ.GetSensorInfo(utils_pb2.SensorId(sensor_id=1))
    print(MessageToJson(res))
    res = observ.GetObjectInfo(utils_pb2.ObjectId(object_id=2))
    print(MessageToJson(res))
    # res = observ.CreateObject(objects_pb2.ObjectCreate(
    #     name="testname",
    #     meta="testmeta",
    #     address="testadress",
    # ))
    # print(MessageToJson(res))
    # res = observ.CreateController(objects_pb2.ControllerCreate(
    #     meta="testmeta",
    #     controller_type=1,
    #     mac="61:72:29:cf:1a:59",
    # ))
    # print(MessageToJson(res))
    res = observ.CreateSensor(objects_pb2.SensorCreate(
        sensor_type=1,
        name="testname",
        controller_id=60,
        company="1",
        date=datetime.datetime.now().strftime("%Y-%m-%d"),
        meta="testmeta",
    ))
    print(MessageToJson(res))
