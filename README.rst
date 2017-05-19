    ZEBU  /ˈzeɪbuː/ - Bos primigenius indicus or Bos indicus or Bos taurus indicus
    sometimes known as indicine cattle or humped cattle, is a species or subspecies of domestic cattle originating 
    in South Asia. Zebu are characterised by a fatty hump on their shoulders, a large dewlap, and sometimes drooping 
    ears. They are well adapted to withstanding high temperatures, and are farmed throughout the tropical countries, 
    both as pure zebu and as hybrids with taurine cattle, the other main type of domestic cattle. Zebu are used as 
    draught oxen, dairy cattle, and beef cattle, as well as for byproducts such as hides and dung for fuel and manure. 
    In 1999, researchers at Texas A&M University successfully cloned a zebu.
    https://en.wikipedia.org/wiki/Zebu

Minibus was taken, since I am French and ZEBU relies on 0MQ I thought thebus pronounced zebus could be a cool name. 
Of course, I could not resist the temptation to name this module after a cow.

Ze service
==========

ZEBU is a uber minimalistic bus which I implemented for fun and turned out to be useful (to me at least).

To run ZEBU you need to set 2 environment variables. 
ZEBU_PUBLISH is the endpoint the publishers connect to.
ZEBU_SUBSCRIBE the endpoint the subscribers connect to. 

Endpoints have the format transport://address where transport would more than likely be ipc or tcp.

$ ZEBU_PUBLISH=ipc://publish ZEBU_SUBSCRIBE=ipc://subscribe python -m zebu

Ze module
=========

ZEBU is also a module you can import to use carefully crafted helpers to define ...

Subscribers
-----------

>>> from zebu import subscribe
>>> messages = subscribes('a/topic', 'another/topic')
>>> for message in messages:
...     # do something with message

Publishers
----------

>>> from zebu import publisher
>>> publish = publisher()
>>> publish('a/topic', 'a message on that topic')