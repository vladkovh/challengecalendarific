import requests

from urllib.parse import urljoin

from settings import CALENDAR_API_KEY, BASE_CALENDAR_API_URL


class CalendarApiRequester:
    def __init__(self):
        self.base_url = BASE_CALENDAR_API_URL

    def get_holidays(self, country, year, month, day):
        url = urljoin(self.base_url, "holidays")
        return requests.get(url, params={
            "api_key": CALENDAR_API_KEY,
            "country": country,
            "year": year,
            "month": month,
            "day": day,
        })
