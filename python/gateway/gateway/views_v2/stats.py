from gateway.views.base_view import BaseMesssage

class SensorStats(BaseMesssage):
    def __init__(self, month, prev_month, prev_year):
        self.month = month 
        self.prev_month = prev_month
        self.prev_year = prev_year

    def _get_msg(self):
        return dict(month=self.month,
                    prev_month=self.prev_month,
                    prev_year=self.prev_year)
