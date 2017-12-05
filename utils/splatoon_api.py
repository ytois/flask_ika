from urllib.parse import urljoin
import requests
import json


class SplatoonApi:
    HOST = 'https://app.splatoon2.nintendo.net/api/'

    def __init__(self, iksm_session):
        self.cookie = {"iksm_session": iksm_session}

    def results(self):
        endpoint = './results'
        return self.__get(endpoint)

    def schedules(self):
        endpoint = './schedules'
        return self.__get(endpoint)

    def timeline(self):
        endpoint = './'
        return self.__get(endpoint)

    def stage_data(self):
        endpoint = './data/stages'
        return self.__get(endpoint)

    def records(self):
        endpoint = './records'
        return self.__get(endpoint)

    def onlineshop(self):
        endpoint = './onlineshop/merchandises'
        return self.__get(endpoint)

    def __get(self, endpoint):
        url = urljoin(self.HOST, endpoint)
        response = requests.get(url, cookies=self.cookie)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return response
