import os
import requests

from requests.auth import HTTPBasicAuth

class Request:


    def __init__(self):
        self.username = self.password = None


    def update(self, username, password):
        self.username = username
        self.password = os.getenv(password)


    def send_request(self, url):
        if self.username is not None and self.password is not None:     
            return requests.get(
                url,
                auth = HTTPBasicAuth(self.username, self.password)
            )
        else:
            return requests.get(url)
