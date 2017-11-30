from urllib.request import build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar
from urllib.parser import urljoin
import codecs


class SplatoonApi:
    HOST = 'https://app.splatoon2.nintendo.net/api'

    def __init__(self, iksm_session):
        self.cookie = "iksm_session={}".format(iksm_session)

    def results(self):
        endpoint = '/results'
        return self.__get(endpoint)

    def __get(self, endpoint):
        url = urljoin(self.HOST, endpoint)
        opener = build_opener(HTTPCookieProcessor(CookieJar()))
        opener.addheaders.append(("Cookie", self.cookie))
        res = opener.open(url)
        return (codecs.decode(res.read(), 'unicode-escape'))
