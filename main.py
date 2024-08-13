import datetime

from request import CalendarApiRequester
from writer import HolidaysWriter


def main():
    # input data
    country_list = ["us", "ua"]
    start_date = datetime.date(1992, 7, 7)
    end_date = datetime.date(1992, 9, 18)

    date_shift = datetime.timedelta(days=1)
    requester = CalendarApiRequester()
    for country in country_list:
        country_holidays = []
        date = start_date
        while date <= end_date:
            response_json = requester.get_holidays(country, date.year, date.month, date.day).json()
            holidays = response_json["response"]["holidays"]
            country_holidays.extend(holidays)
            date += date_shift
        writer = HolidaysWriter(start_date, end_date, country, country_holidays)
        writer.write_country_holidays_to_file()


if __name__ == "__main__":
    main()







