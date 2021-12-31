from textindexer.database import DocsDatabase
from textindexer.server.models.document_record import DocumentRecord  # noqa: E501
import connexion


def get_indexer_v1_document(skip=None, limit=None, status=None):  # noqa: E501
    """Your GET endpoint

    Get a list of document records # noqa: E501

    :param skip: 
    :type skip: int
    :param limit: 
    :type limit: int

    :rtype: Documents
    """
    docs_db = DocsDatabase()
    return docs_db.get_documents(skip=skip, limit=limit, status=status)


def post_indexer_v1_document(document_record=None):
    """post_indexer_v1_document

    Add a document record # noqa: E501

    :param document_record: 
    :type document_record: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        document_record = DocumentRecord.from_dict(connexion.request.get_json())  # noqa: E501
        docs_db = DocsDatabase()
        docs_db.add_document(document_record.to_dict())
    return None

