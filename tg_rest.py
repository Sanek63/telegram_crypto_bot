import time
from typing import BinaryIO

import requests
import json

from config import TOKEN, WAIT_SECONDS, MAX_RETRIES


# import logging
# from http.client import HTTPConnection


# log = logging.getLogger('urllib3')
# log.setLevel(logging.DEBUG)
#
# # logging from urllib3 to console
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# log.addHandler(ch)
#
# # print statements from `http.client.HTTPConnection` to console/stdout
# HTTPConnection.debuglevel = 1

def _handling_request_error(function):
    def execute_function(*args, **kwargs):
        for _ in range(MAX_RETRIES):
            try:
                return function(*args, **kwargs)
            except requests.exceptions.RequestException:
                time.sleep(WAIT_SECONDS)
                continue
        return SystemError("System error")

    return execute_function


class TgRest:
    def __init__(self):
        self.base_endpoint = "https://{}/bot{}".format("api.telegram.org", TOKEN)
        self.access_token = None

    def get(self, uri, params=None, headers={}):
        return requests.get("{}/{}".format(self.base_endpoint, uri), params, headers=headers)

    def post(self, uri, data=None, headers={}):
        data_json = None
        if data is not None:
            data_json = json.dumps(data)

        headers_req = headers.copy()
        headers_req['Content-Type'] = 'application/json'

        return requests.post("{}/{}".format(self.base_endpoint, uri), json=data, headers=headers_req)

    @_handling_request_error
    def send_msg(self, user_id: int, text_msg: str, headers={}):
        r = requests.get(
            "{}/{}".format(self.base_endpoint, "sendMessage"),
            params={"chat_id": user_id, "text": text_msg}
        )

    @_handling_request_error
    def send_photo(self, chat_id: int, file_bytes: BinaryIO):
        r = requests.post(
            "{}/{}".format(self.base_endpoint, "sendPhoto"),
            params={"chat_id": chat_id},
            files={"photo": file_bytes}
        )
