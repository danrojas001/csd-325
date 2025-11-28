# Dan Rojas
# 27 Nov 2025
# Mod 9.2
##############

# Contains both astronaut API functions(DISABLED) and Advice API functions. Tests API, then prints random piece of
# advice (unformatted and formatted).

import sys
import requests
import json

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 13
astros_url = 'http://api.open-notify.org/astros.json'  # worked without .json as well.
advice_url = 'https://api.adviceslip.com/advice'


def main():
    check_python_version()
    # test_astronauts_api()
    # get_astronauts_in_space()
    test_advice_api()
    get_advice()


"""ASTRONAUTS API"""


def test_astronauts_api():
    response = requests.get(astros_url)
    print(f'Response status code for http://api.open-notify.org/astros.json: {response.status_code}\n')


def get_astronauts_in_space():
    response = requests.get(astros_url)
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(f"{response.json()}\n")
    print(f"{text}\n")


"""ADVICE API"""


def test_advice_api():
    response = requests.get(advice_url)
    print(f'Response status code for https://api.adviceslip.com/: {response.status_code}\n')


def get_advice():
    response = requests.get(advice_url)
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(f"{response.json()}\n")
    print(f"{text}\n")


# Python version check
def check_python_version():
    current_major = sys.version_info.major
    current_minor = sys.version_info.minor

    if current_major != REQUIRED_MAJOR or current_minor < REQUIRED_MINOR:
        print(
            f"Python version mismatch: This script was written with Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}"
            f", but you are running {current_major}.{current_minor}."
        )
        print("Please consider upgrading your Python version for full compatibility.")
        print()
    else:
        print(f"Python version {current_major}.{current_minor} is compatible.")
        print()


if __name__ == "__main__":
    main()
