#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    print("{} argument{}{}".format(
        argc, "" if argc == 1 else "s", ":" if argc else "."))
    for i, v in enumerate(argv):
        if not i == 0:
            print("{}: {}".format(i, v))
