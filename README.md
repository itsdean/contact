# contact

abstract: git commits are relatively simple way of obtaining emails for OSINT purposes.

this leverages GitHub APIs to go through a target user or organisation's repositories, extracting email addresses and names from every commit.

## usage

out of the box:
```
./contact.py --target <user/org>
```

if you need to auth, provide your username and the name of an environment variable storing your GitHub Personal Access Token:
```
./contact.py --target <user/org> --username <your GitHub login> --token <environment variable name>
```

you can also use `--url` if you're connecting to a non GitHub.com server:
```
./contact.py --url https://lorenipsum.com --target <user/org>
```
