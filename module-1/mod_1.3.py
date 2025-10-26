# Dan Rojas
# 26 Oct 2025
# Mod 1.3
##############

# Requests a positive integer value. Validates the value, produces lyrics for "Bottle of beer".

import sys

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 13


def main():
    check_python_version()
    bottles_of_beer()


def bottles_of_beer():
    beer_num = gather_beer_bottles()
    beer_counter(beer_num)


def gather_beer_bottles():
    while True:
        try:
            num = int(input("Enter the number of bottles of beer you want: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def beer_counter(num):
    if num == 1:
        print(f"{num} bottle of beer on the wall, {num} bottle of beer.\n"
              f"Take one down, pass it around, {num} bottle of beer on the wall.\n\n"
              f"Time to buy more bottles of beer.")
    else:
        print(f"{num} bottles of beer on the wall, {num} bottles of beer.\n"
              f"Take one down, pass it around, {num} bottles of beer on the wall.\n")
        num = num - 1
        beer_counter(num)


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
