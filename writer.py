import json
import os

from settings import HOLIDAYS_SUBDIR


class HolidaysWriter:
    def __init__(self, start_date, end_date, country_code, holidays):
        self.start_date = start_date
        self.end_date = end_date
        self.country_code = country_code
        self.holidays = holidays
        self.working_dir = os.getcwd()
        self.holidays_subdir_path = os.path.join(self.working_dir, HOLIDAYS_SUBDIR)
        os.makedirs(self.holidays_subdir_path, exist_ok=True)

    def write_country_holidays_to_file(self):
        filename = "{}_{}_{}.txt".format(
            self.country_code,
            self.start_date.strftime("%Y-%d-%m"),
            self.end_date.strftime("%Y-%d-%m")
        )
        with open(os.path.join(self.holidays_subdir_path, filename), 'w') as f:
            json.dump(self.holidays, f)
