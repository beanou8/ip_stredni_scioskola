import datetime
from datetime import date


class Medication:
    def __init__(self, date_bought, packaging_size, dosage):
        self.date = date_bought
        self.packaging_size = packaging_size
        self.dosage = dosage

    def get_final_date(self):
        days = datetime.timedelta(self.packaging_size / self.dosage)
        final_date = self.date + days
        return final_date.strftime("%d.%m.%Y")


derin = Medication(date(2022, 3, 22), 180, 4)
print('Derin mi dojde:', derin.get_final_date())
