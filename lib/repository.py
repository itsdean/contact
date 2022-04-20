class Repository:
    def parse_commits(self):
        response = self.r.send_request(self.commits_url)
        commits = response.json()

        for commit in commits:
            commit = commit["commit"]

            author = commit["author"]
            a_name = author["name"]
            a_email = author["email"]
            self.l.add(self.name, a_name, a_email)

            committer = commit["committer"]
            c_name = committer["name"]
            c_email = committer["email"]
            self.l.add(self.name, c_name, c_email)

    def __init__(self, request, loot, repository):

        self.r = request
        self.l = loot

        self.name = repository["name"]

        self.url = repository["url"]
        self.commits_url = f"{self.url}/commits"

        # store if repo is a fork
        self.fork = repository["fork"]

        if not self.fork:
            self.parse_commits()
