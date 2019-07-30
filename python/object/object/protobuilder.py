import proto.objects_pb2_grpc as objects_pb2_grpc
import proto.objects_pb2 as objects_pb2
import proto.utils_pb2 as utils_pb2
import time
import logging


def build_user_pb(data):
    objs = [build_object_pb(obj) for obj in data["objects"].values()]
    return objects_pb2.UserInfoH(
        id=utils_pb2.UserId(
            user_id=data["id"]
        ),
        objects=objs
    )


def build_object_pb(data):
    controllers = [build_controller_pb(ctrl) for ctrl in data["controllers"].values()]
    return objects_pb2.ObjectInfo(
        id=utils_pb2.ObjectId(
            object_id=data["id"],
        ),
        name=data["name"],
        address=data["address"],
        controllers=controllers,
        user_id=utils_pb2.UserId(user_id=data["user_id"],),
        meta=data["meta"]
    )


def build_controller_pb(data):
    sensors = [build_sensor_pb(snsr) for snsr in data["sensors"].values()]
    ctrl_info = objects_pb2.ControllerInfo(
        id=utils_pb2.ControllerId(
            controller_id=data["id"],
        ),
        sensors=sensors,
        meta=data["meta"],
        name=data["name"],
        controller_type=data["controller_type"],
        object_id=utils_pb2.ObjectId(
            object_id=data["object_id"],
        ),
    )
    if data["deactivation_date"] is not None:
        ctrl_info.deactivation_date_val = int(time.mktime(data["deactivation_date"].timetuple()))

    if data["activation_date"] is not None:
        ctrl_info.activation_date_val = int(time.mktime(data["activation_date"].timetuple()))
    return ctrl_info


def build_sensor_pb(data):
    logging.debug(data)
    sens_inf = objects_pb2.SensorInfo(
        id=utils_pb2.SensorId(sensor_id=data["id"]),
        status=data["status"],
        meta=data["meta"],
        sensor_type=data["sensor_type"],
        controller_id=utils_pb2.ControllerId(controller_id=data["controller_id"]),
        company=data["company"],
        name=data["name"],
    )
    if data["deactivation_date"] is not None:
        sens_inf.deactivation_date_val = int(time.mktime(data["deactivation_date"].timetuple()))
    if data["activation_date"] is not None:
        sens_inf.activation_date_val = int(time.mktime(data["activation_date"].timetuple()))
    return sens_inf
