import connexion
import six

from textindexer.server.models.document_index import DocumentIndex  # noqa: E501
from textindexer.server.models.document_record import DocumentRecord  # noqa: E501
from textindexer.server.models.documents import Documents  # noqa: E501
from textindexer.server.models.words import Words  # noqa: E501
from textindexer.server import util


def get_indexer_v1_document(skip=None, limit=None):  # noqa: E501
    """Your GET endpoint

    Get a list of document records # noqa: E501

    :param skip: 
    :type skip: int
    :param limit: 
    :type limit: int

    :rtype: Documents
    """
    return 'do some magic!'


def get_indexer_v1_document_doc(doc_id):  # noqa: E501
    """Your GET endpoint

    Get the document record # noqa: E501

    :param doc_id: 
    :type doc_id: str

    :rtype: DocumentRecord
    """
    return 'do some magic!'


def get_indexer_v1_document_doc_id_full(doc_id):  # noqa: E501
    """Your GET endpoint

    Get the document with the full text enabled # noqa: E501

    :param doc_id: 
    :type doc_id: str

    :rtype: DocumentRecord
    """
    return 'do some magic!'


def get_indexer_v1_document_doc_id_index(doc_id):  # noqa: E501
    """Your GET endpoint

    Get the index record related to the document # noqa: E501

    :param doc_id: 
    :type doc_id: str

    :rtype: DocumentIndex
    """
    return 'do some magic!'


def get_indexer_v1_words(skip=None, limit=None, reverse=None):  # noqa: E501
    """Your GET endpoint

     # noqa: E501

    :param skip: 
    :type skip: int
    :param limit: 
    :type limit: int
    :param reverse: 
    :type reverse: bool

    :rtype: Words
    """
    return 'do some magic!'


def post_indexer_v1_document(document_record=None):  # noqa: E501
    """post_indexer_v1_document

    Add a document record # noqa: E501

    :param document_record: 
    :type document_record: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        document_record = DocumentRecord.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


from .default_controller_implementation import *
