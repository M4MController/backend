class Passport(object):
    def __init__(self, issued_by, date_receiving, division_number):
        self.issued_by = issued_by
        self.date_receiving = date_receiving
        self.division_number = division_number

    def get_fields(self):
        return {
            "issued_by": self.issued_by,
            "date_receiving": self.date_receiving,
            "division_number": self.division_number,
        }
