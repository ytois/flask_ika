from urllib.parse import urljoin
import requests
import json


class SplatoonApi:
    HOST = 'https://app.splatoon2.nintendo.net/api/'

    def __init__(self, iksm_session):
        self.cookie = {"iksm_session": iksm_session}

    def results(self, battle_number=None):
        if battle_number:
            endpoint = './results/%s' % battle_number
        else:
            endpoint = './results'
        return self._get(endpoint)

    def schedules(self):
        endpoint = './schedules'
        return self._get(endpoint)

    def timeline(self):
        endpoint = './'
        return self._get(endpoint)

    def stage_data(self):
        endpoint = './data/stages'
        return self._get(endpoint)

    def records(self):
        endpoint = './records'
        return self._get(endpoint)

    def onlineshop(self):
        endpoint = './onlineshop/merchandises'
        return self._get(endpoint)

    def _get(self, endpoint):
        url = urljoin(self.HOST, endpoint)
        response = requests.get(url, cookies=self.cookie)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return response
