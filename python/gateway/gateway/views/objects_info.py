from gateway.views.base_view import BaseMesssage


class UserInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, objects):
        super(UserInfo, self).__init__(self)
        self.id = id
        self.objects = objects

    def _get_msg(self):
        return dict(id=self.id,
                    objects=[i._get_msg() for i in self.objects])

class ObjectInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, name, address, controllers):
        super(ObjectInfo, self).__init__(self)
        self.id = id
        self.name = name
        self.address = address
        self.controllers = controllers

    def _get_msg(self):
        return dict(id=self.id,
                    name=self.name,
                    address=self.address,
                    controllers=[i._get_msg() for i in self.controllers])

class ControllerInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, name, meta, activation_date, status, mac, controller_type,deactivation_date, sensors):
        super(ControllerInfo, self).__init__(self)
        self.id= id
        self.name = name
        self.meta = meta
        self.activation_date = activation_date
        self.status = status
        self.mac = mac
        self.controller_type = controller_type
        self.deactivation_date = deactivation_date
        self.sensors = sensors

    def _get_msg(self):
        return dict(id = self.id, 
                    name = self.name,
                    meta = self.meta, 
                    activation_date = self.activation_date,
                    status = self.status,
                    mac = self.mac,
                    controller_type = self.controller_type,
                    deactivation_date = self.deactivation_date,
                    sensors = [ i._get_msg() for i in self.sensors])

class SensorInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, name, activation_date, deactivation_date, sensor_type, company):
        super(SensorInfo, self).__init__(self)
        self.id = id
        self.name = name
        self.activation_date = activation_date
        self.deactivation_date = deactivation_date
        self.sensor_type = sensor_type
        self.company = company

    def _get_msg(self):
        return {"id": self.id,
                "name": self.name,
                "activation_date": self.activation_date,
                "deactivation_date": self.deactivation_date,
                "sensor_type": self.sensor_type,
                "company": self.company}