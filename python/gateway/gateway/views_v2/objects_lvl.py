from gateway.views.base_view import BaseMesssage

class Listed(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, objects):
        super(Listed, self).__init__(self)
        self.objects = objects

    def _get_msg(self):
        return[i._get_msg() for i in self.objects]

class ObjectInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, user_id, name, address, payments):
        super(ObjectInfo, self).__init__(self)
        self.id = id
        self.name = name
        self.address = address
        self.user_id = user_id
        self.payments = payments

    def _get_msg(self):
        return dict(id=self.id,
                    name=self.name,
                    user_id=self.user_id,
                    address=self.address,
                    payments=self.payments._get_msg())

class ControllerInfo(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self, id, object_id, name, meta, activation_date, status, mac, controller_type, deactivation_date, payments):
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
        self.payments = payments

    def _get_msg(self):
        res = dict(id=self.id,
                   name=self.name,
                   meta=self.meta,
                   object_id=self.object_id,
                   activation_date=self.activation_date,
                   status=self.status,
                   mac=self.mac,
                   controller_type=self.controller_type,
                   deactivation_date=self.deactivation_date,
                   payments=self.payments._get_msg())
        #if self.deactivation_date is not None:
        #    res.update({"deactivation_date": self.deactivation_date})
        #if self.activation_date is not None:
        #    res.update({"activation_date": self.activation_date})
        return res

class CompanyView(BaseMesssage):
    def __init__(self, _id, name, address, phone, bank_account_id):
        self.id = _id
        self.name = name
        self.address = address
        self.phone = phone
        self.bank_account_id = bank_account_id

    def _get_msg(self):
        return dict(
            id=self.id,
            name=self.name,
            address=self.address,
            phone=self.phone,
            bank_account_id=self.bank_account_id)

class SensorFinance(BaseMesssage):
    def __init__(self, tariff, payment_id, service_company):
        self.tariff = tariff
        self.payment_id = payment_id
        self.service_company = service_company

    def _get_msg(self):
        return dict(
            tariff=self.tariff._get_msg(),
            payment_id=self.payment_id,
            service_company=self.service_company._get_msg())


class SensorCharacteristics(BaseMesssage):
    def __init__(self, sensor_type, unit_of_measurement):
        self.sensor_type = sensor_type
        self.unit_of_measurement = unit_of_measurement
    
    def _get_msg(self):
        return dict(
            sensor_type=self.sensor_type,
            unit_of_measurement=self.unit_of_measurement)


class SensorInfo(BaseMesssage):
    error_code = 0
    http_code = 200

    def __init__(self,
                 id,
                 controller_id,
                 name,
                 activation_date,
                 deactivation_date,
                 stats,
                 payments,
                 characteristics,
                 finance,
                 meta,
                 status=0,
                 last_value=0,
                 user_id=None):
        super(SensorInfo, self).__init__(self)
        self.id = id
        self.name = name
        self.activation_date = activation_date
        self.deactivation_date = deactivation_date
        self.finance = finance
        self.characteristics = characteristics
        self.controller_id = controller_id
        self.last_value = last_value
        self.stats = stats
        self.payments = payments
        self.user_id = user_id
        self.meta = meta

    def _get_msg(self):
        res = dict(id=self.id,
                   name=self.name,
                   activation_date=self.activation_date,
                   deactivation_date=self.deactivation_date,
                   controller_id=self.controller_id,
                   last_value=self.last_value,
                   finance=None if self.finance is None else self.finance._get_msg(),
                   characteristics=None if self.characteristics is None else self.characteristics._get_msg(),
                   stats=self.stats._get_msg() if hasattr(self.stats, "_get_msg") else None,
                   payments=None if self.payments is None else self.payments._get_msg(),
                   user_id=self.user_id,
                   meta=self.meta)
        # if self.last_value is not None:
        #     res.update({"last_value": self.last_value})
        return res


class ObjList(BaseMesssage):
    error_code = 0
    http_code = 200

    def __init__(self, *args, **kwargs):
        super(ObjList, self).__init__(self)
        self.info = kwargs

    def _get_msg(self):
        return {i: j._get_msg() for i, j in self.info.items() if j is not None}


class UserInfo(BaseMesssage):
    error_code = 0
    http_code = 200

    def __init__(self,
                 _id,
                 family_name,
                 name,
                 second_name,
                 date_receiving,
                 issued_by,
                 division_number,
                 registration_addres,
                 mailing_addres,
                 birth_day,
                 sex,
                 home_phone,
                 mobile_phone,
                 citizenship,
                 e_mail):
        super(UserInfo, self).__init__(self)
        self._id = _id
        self.family_name = family_name
        self.name = name
        self.second_name = second_name
        self.date_receiving = date_receiving
        self.issued_by = issued_by
        self.division_number = division_number
        self.registration_addres = registration_addres
        self.mailing_addres = mailing_addres
        self.birth_day = birth_day
        self.sex = sex
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.citizenship = citizenship
        self.e_mail = e_mail

    def _get_msg(self):
        res = dict(id=self._id,
                   family_name=self.family_name,
                   name=self.name,
                   second_name=self.second_name,
                   date_receiving=self.date_receiving,
                   issued_by=self.issued_by,
                   division_number=self.division_number,
                   registration_addres=self.registration_addres,
                   mailing_addres=self.mailing_addres,
                   birth_day=self.birth_day,
                   sex=self.sex,
                   home_phone=self.home_phone,
                   mobile_phone=self.mobile_phone,
                   citizenship=self.citizenship,
                   e_mail=self.e_mail,)
        return res
