#!/usr/bin/env python3

# Import external libraries
import argparse

# Import internal libraries
from lib.target import Target


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--method",
    #     help = "the method of accessing the target's git repositories",
    #     default = "remote"
    # )
    parser.add_argument("--target", help="the target user/organisation", required=True)
    parser.add_argument(
        "--url",
        help="the location of the vcs' api (if not api.github.com)",
        default="https://api.github.com",
    )
    parser.add_argument(
        "--username",
        help="the name of your account (if authentication is required due to rate limiting). also requires --token",
        default="",
    )
    parser.add_argument(
        "--token",
        help="the name of the environment variable storing a GitHub PAT. also requires --username",
        default="",
    )

    # Store the values in individual variables
    values = parser.parse_args()
    t = Target(values)
    t.go()
    t.report()


if __name__ == "__main__":
    print("\ncontact.py - https://github.com/itsdean\n")
    main()
    print()
