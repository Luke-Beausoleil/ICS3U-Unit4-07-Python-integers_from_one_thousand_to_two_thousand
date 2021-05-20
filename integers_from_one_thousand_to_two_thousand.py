#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program prints integers from 1000 - 2000


def main():
    # this function prints the integers

    # process & output
    for integer in range(1000, 2000 + 1):
        if integer % 5 != 0:
            print("{0} ".format(integer), end="")
        else:
            print("\n{0} ".format(integer), end="")


if __name__ == "__main__":
    main()
