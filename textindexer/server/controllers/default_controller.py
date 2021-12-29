import connexion
import six

from textindexer.server.models.document import Document  # noqa: E501
from textindexer.server.models.inline_object import InlineObject  # noqa: E501
from textindexer.server.models.inline_response200 import InlineResponse200  # noqa: E501
from textindexer.server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from textindexer.server import util


def get_indexer_v1_document():  # noqa: E501
    """Your GET endpoint

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_indexer_v1_document_doc_id(doc_id):  # noqa: E501
    """Your GET endpoint

     # noqa: E501

    :param doc_id: 
    :type doc_id: str

    :rtype: Document
    """
    return 'do some magic!'


def get_indexer_v1_document_doc_id_raw(doc_id):  # noqa: E501
    """Your GET endpoint

     # noqa: E501

    :param doc_id: 
    :type doc_id: str

    :rtype: Document
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

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def post_indexer_v1_document(filename=None, encoding=None, language=None, inline_object=None):  # noqa: E501
    """post_indexer_v1_document

     # noqa: E501

    :param filename: 
    :type filename: str
    :param encoding: 
    :type encoding: str
    :param language: 
    :type language: str
    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
