import queue
import logging
from pymongo import MongoClient
from amqpstorm import Connection

class PostProcessor():

    def __init__(self, mongo={}, mq={}):
        logging.warning("Mongo:{}".format(mongo))
        logging.warning("MQ:{}".format(mq))
        self._db = MongoClient(
            mongo.get('host'),
            username=mongo.get('username'),
            password=mongo.get('password'))
        self._mq = Connection(
            mq.get('host'),
            username=mq.get('username'),
            password=mq.get('password'))

    def test(self):
        databases = self._db.list_databases()
        properties = self._mq.server_properties
        logging.warning("Databases:{}".format(databases))
        logging.warning("MQ Props:{}".format(properties))
