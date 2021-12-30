import queue
import logging
from pymongo import MongoClient
from amqpstorm import Connection

class PostProcessor():

    def __init__(self, mongo={}, mq={}):
        self._mongo_username = mongo.get('username')
        self._mongo_username = mongo.get('password')
        self._mongo_host = mongo.get('host')
        self._mq_username = mq.get('username')
        self._mq_username = mq.get('password')
        self._mq_host = mq.get('host')
        self._db = MongoClient(
            mongo.get('host'),
            username=mongo.get('username'),
            password=mongo.get('password'))
        self._mq = Connection(
            hostname=mq.get('host'),
            username=mq.get('username'),
            password=mq.get('password'))

    def test(self):
        databases = self._db.list_databases()
        properties = self._mq.server_properties
        logging.warning("Databases:{}".format(databases))
        logging.warning("MQ Props:{}".format(properties))
