class Loot:

    IGNORED_EMAILS = [
        "noreply@github.com"
    ]

    IGNORED_PHRASES = [
        "noreply.github.com"
    ]


    def count(self):
        return len(self.bag)
             

    def add(self, repo, name, email):
        acceptable = True

        for phrase in self.IGNORED_PHRASES:
            if phrase in email:
                acceptable = False

        if email in self.IGNORED_EMAILS:
            acceptable = False

        if acceptable:
            if email not in self.bag.keys():
                self.bag[email] = {
                    "names": {
                        name: [repo]
                    }
                }
            else:
                # if the name tied with the email already exists,
                if name in self.bag[email]["names"].keys():
                    # check if the repo has been tied to the name
                    if repo not in self.bag[email]["names"][name]:
                        self.bag[email]["names"][name].append(repo)
                else:
                    self.bag[email]["names"][name] = [repo]

    def __init__(self):
        self.bag = {}