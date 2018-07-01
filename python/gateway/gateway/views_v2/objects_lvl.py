from gateway.views.base_view import BaseMesssage

class Listed(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, objects):
        super(Listed, self).__init__(self)
        self.objects = objects

    def _get_msg(self):
        return dict(objects=[i._get_msg() for i in self.objects])

class ObjectInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, user_id, name, adres):
        super(ObjectInfo, self).__init__(self)
        self.id = id
        self.name = name
        self.adres = adres
        self.user_id = user_id

    def _get_msg(self):
        return dict(id=self.id,
                    name=self.name,
                    user_id=self.user_id,
                    adres=self.adres)

class ControllerInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, object_id, name, meta, activation_date, status, mac, controller_type,deactivation_date):
        super(ControllerInfo, self).__init__(self)
        self.id= id
        self.name = name
        self.meta = meta
        self.activation_date = activation_date
        self.status = status
        self.mac = mac
        self.controller_type = controller_type
        self.deactivation_date = deactivation_date
        self.object_id = object_id

    def _get_msg(self):
        return dict(id = self.id, 
                    name = self.name,
                    meta = self.meta,
                    object_id = self.object_id,
                    activation_date = self.activation_date,
                    status = self.status,
                    mac = self.mac,
                    controller_type = self.controller_type,
                    deactivation_date = self.deactivation_date)

class SensorInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, controller_id, name, activation_date, deactivation_date, sensor_type, company, last_value=0):
        super(SensorInfo, self).__init__(self)
        self.id = id
        self.name = name
        self.activation_date = activation_date
        self.deactivation_date = deactivation_date
        self.sensor_type = sensor_type
        self.company = company
        self.controller_id = controller_id
        self.last_value = last_value

    def _get_msg(self):
        return dict(id = self.id,
                name = self.name,
                activation_date = self.activation_date,
                deactivation_date = self.deactivation_date,
                sensor_type = self.sensor_type,
                controller_id = self.controller_id,
                company = self.company,
                last_value = self.last_value)

class ObjList(BaseMesssage):
    error_code = 0
    http_code = 200

    def __init__(self, *args, **kwargs):
        super(ObjList, self).__init__(self)
        self.info = kwargs
    
    def _get_msg(self):
        return  {i:j._get_msg() for i,j in self.info.items()}