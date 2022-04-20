import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import repeat

import requests

from .loot import Loot
from .repository import Repository
from .request import Request


class Target:
    def check(self, target):

        response = self.r.send_request(self.target_endpoint)

        # the api should return json
        if "application/json" not in response.headers["content-type"]:
            print("content-type is incorrect, was expecting application/json")
            exit()

        # logic to check if the target exists
        if response.status_code != 200:
            if response.json()["message"] == "Not Found":
                print("target not found")
            else:
                print(
                    f"did not receive a 200 for {self.url}, received {response.status_code} instead"
                )
                print(response.json())
            exit()

        # check if the target is a user or an org
        if response.json()["type"] == "User":
            return "user"
        else:
            return "org"

    def __append_repository(self, request, loot, repo):
        self.repositories.append(Repository(request, loot, repo))

    def parse_repositories(self):
        self.repositories = []

        response = self.r.send_request(f"{self.target_endpoint}/repos")

        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(
                self.__append_repository,
                repeat(self.r),
                repeat(self.l),
                response.json(),
            )

    def report(self):
        print(
            f"\nfound {self.l.count()} email(s) within {len(self.repositories)} repo(s)"
        )
        for key in self.l.bag.keys():
            print(f"email: {key}")
            for name in self.l.bag[key]["names"]:
                print(f"> name: {name} [{', '.join(self.l.bag[key]['names'][name])}]")

    def go(self):
        self.parse_repositories()

    def __init__(self, values):
        self.r = Request()
        self.l = Loot()

        self.url = values.url

        self.target = values.target
        print(f"target is {self.target}")

        if values.username != "" and values.token != "":
            self.r.update(values.username, values.token)

        self.target_endpoint = f"{self.url}/users/{self.target}"

        # check if target is user or org
        self.type = self.check(self.target)
        print(f"type is {self.type}")
