import logging
from pymongo import MongoClient
from bson.json_util import dumps
import os
import json


class DocsDatabase():

    _DATABASE = 'indexer'
    _DOCUMENTS_COLLECTION = 'documents'
    _INDEXES_COLLECTION = 'indexed'
    _WORDS_COLLECTION = 'words'

    def __init__(self, mongo={}):
        mongo_config = {
            'host': os.environ.get(
                'MONGO_HOST',
                mongo.get('host','mongo')),
            'username': os.environ.get(
                'MONGO_INITDB_ROOT_USERNAME',
                mongo.get('username','mongo')),
            'password': os.environ.get(
                'MONGO_INITDB_ROOT_PASSWORD',
                mongo.get('password','mongo'))}
        logging.warning("Mongo Init:{}".format(mongo_config))
        self._db = MongoClient(
            mongo_config.get('host'),
            username=mongo_config.get('username'),
            password=mongo_config.get('password'))[self._DATABASE]
    
    def get_documents(self, skip=0, limit=10, status=None):
        if not isinstance(skip, int) :
            skip = 0
        if not isinstance(limit, int):
            limit = 100
        query = {}
        if status:
            query['status'] = status
        docs_collection = self._db[self._DOCUMENTS_COLLECTION]
        docs = docs_collection.find(query)
        count = docs_collection.count_documents(query)
        docs.skip(skip).limit(limit)
        ret_docs = []
        for i in docs:
            ret_docs.append(self._process_document(i))
        return {
            'count': count,
            'documents': ret_docs}
    
    def add_document(self, document):
        docs_collection = self._db[self._DOCUMENTS_COLLECTION]
        docs_collection.insert_one(document)

    def _process_document(self, doc):
        return json.loads(dumps(doc))