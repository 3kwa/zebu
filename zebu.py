"""
Many publishers many subscribers (using ZeroMQ)

PUSH ... PUSH     cf. http://zguide.zeromq.org/py:taskwork

PULL              cf. http://zguide.zeromq.org/py:tasksink
PUB               cf. http://zguide.zeromq.org/py:wuserver

SUB ... SUB       cf. http://zguide.zeromq.org/py:wuclient

Decided against using XPUB XSUB as I do not want the publishers to know anything
about the subscribers.

The environment variables ZEBU_PUBLISH and ZEBU_SUBSCRIBE use the
ZeroMQ syntax to specify how to bind e.g.

    $ ZEBU_PUBLISH=ipc://publish ZEBU_SUBSCRIBE=ipc://subscribe python -m zebu

Starts the service using IPC (relative to current directory).
"""

import os

import zmq


def publisher():
    """ to publish you need a publisher
    >>> publish = publisher()
    >>> publish('a/topic', 'a message I want to broadcast')
    """
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect(os.environ['ZEBU_PUBLISH'])
    def publish(topic, message):
        """
        publishes a message on a topic
        """
        socket.send_string(f"{topic} {message}")
    return publish

def subscribe(*topics):
    """
    >>> messages = subscribe('a/topic', 'another/topic')
    >>> for message in messages:
    ...     # do something
    """
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(os.environ['ZEBU_SUBSCRIBE'])
    for topic in topics:
        socket.setsockopt_string(zmq.SUBSCRIBE, topic)
    while True:
        yield socket.recv()

def main():
    """
    $ python -m zebu
    """
    context = zmq.Context()
    sink = context.socket(zmq.PULL)
    sink.bind(os.environ['ZEBU_PUBLISH'])
    fan = context.socket(zmq.PUB)
    fan.bind(os.environ['ZEBU_SUBSCRIBE'])
    while True:
        received = sink.recv()
        fan.send(received)

if __name__ == '__main__':
    main()
