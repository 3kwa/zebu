"""
A publisher

$ ZEBU_PUBLISH=ipc://publish python publisher.py integers/from/1/to/99
"""

import sys
import time

from zebu import publisher


def main():
    topic = sys.argv[1]
    publish = publisher()
    for num in range(100):
        time.sleep(.1)
        publish(topic, num)

if __name__ == '__main__':
    main()
