# Dan Rojas
# 18 Nov 2025
# Mod 7.2
##############

# it prints the 3 desired lines containing City, Country for one, City, Country, Population for the next and City,
# Country, Population, Language for the last.
# I wrapped the calls in print statements as it made no sense for me to screencap 'exit code 0' multiple times.

import sys

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 13


def main():
    check_python_version()
    print(city_country("Los Angeles", "USA"))
    print(city_country("New York", "USA", 1000000))
    print(city_country("Miami", "USA", 1000000, "English"))



def city_country(city, country, population=None, language=None):
    if population is None and language is None:
        return "{}, {}".format(city, country)
    elif population is None:
        return "{}, {}, {}".format(city, country, language)
    elif language is None:
        return "{}, {} - {}".format(city, country, population)
    else:
        return "{}, {} - {}, {}".format(city, country, population, language)


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
