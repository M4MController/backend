from gateway.views.base_view import BaseMesssage

class ObjectPayments(BaseMesssage):
    def __init__(self, current_month, prev_year, year_avg):
        self.current_month = current_month 
        self.prev_year = prev_year
        self.year_avg = year_avg

    def _get_msg(self):
        return dict(current_month=self.current_month,
                    prev_year=self.prev_year,
                    year_avg=self.year_avg)

class ControllerPayments(BaseMesssage):
    def __init__(self, charge, overpayment, for_payment):
        self.charge = charge 
        self.overpayment = overpayment
        self.for_payment = for_payment

    def _get_msg(self):
        return dict(charge=self.charge,
                    overpaiment=self.overpayment,
                    for_paiment=self.for_payment)

class SensorPayments(BaseMesssage):
    def __init__(self, charge, overpayment, for_payment):
        self.charge = charge 
        self.overpayment = overpayment
        self.for_payment = for_payment

    def _get_msg(self):
        return dict(charge=self.charge,
                    overpaiment=self.overpayment,
                    for_paiment=self.for_payment)
