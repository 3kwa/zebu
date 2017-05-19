"""
A subscriber

$ ZEBU_SUBSCRIBE=ipc://subscribe python subscriber.py integers/from/1/to/99
"""

import sys

from zebu import subscribe


def main():
    topics = sys.argv[1:]
    messages = subscribe(*topics)
    for message in messages:
        print(message)

if __name__ == '__main__':
    main()
