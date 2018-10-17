from gateway.views.base_view import BaseMesssage

class ObjectPayments(BaseMesssage):
    def __init__(self, charge, overpayment, for_payment):
        self.charge = charge 
        self.overpayment = overpayment
        self.for_payment = for_payment

    def _get_msg(self):
        return dict(charge=self.charge,
                    overpayment=self.overpayment,
                    for_payment=self.for_payment)

class ControllerPayments(BaseMesssage):
    def __init__(self, charge, overpayment, for_payment):
        self.charge = charge 
        self.overpayment = overpayment
        self.for_payment = for_payment

    def _get_msg(self):
        return dict(charge=self.charge,
                    overpayment=self.overpayment,
                    for_payment=self.for_payment)

class SensorPayments(BaseMesssage):
    def __init__(self, charge, overpayment, for_payment):
        self.charge = charge 
        self.overpayment = overpayment
        self.for_payment = for_payment

    def _get_msg(self):
        return dict(charge=self.charge,
                    overpayment=self.overpayment,
                    for_payment=self.for_payment)
