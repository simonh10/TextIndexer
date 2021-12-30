# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from textindexer.server.models.base_model_ import Model
from textindexer.server.models.document_index_paragraphs import DocumentIndexParagraphs
from textindexer.server import util

from textindexer.server.models.document_index_paragraphs import DocumentIndexParagraphs  # noqa: E501

class DocumentIndex(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, paragraphs=None, source=None):  # noqa: E501
        """DocumentIndex - a model defined in OpenAPI

        :param id: The id of this DocumentIndex.  # noqa: E501
        :type id: str
        :param paragraphs: The paragraphs of this DocumentIndex.  # noqa: E501
        :type paragraphs: List[DocumentIndexParagraphs]
        :param source: The source of this DocumentIndex.  # noqa: E501
        :type source: str
        """
        self.openapi_types = {
            'id': str,
            'paragraphs': List[DocumentIndexParagraphs],
            'source': str
        }

        self.attribute_map = {
            'id': 'id',
            'paragraphs': 'paragraphs',
            'source': 'source'
        }

        self._id = id
        self._paragraphs = paragraphs
        self._source = source

    @classmethod
    def from_dict(cls, dikt) -> 'DocumentIndex':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DocumentIndex of this DocumentIndex.  # noqa: E501
        :rtype: DocumentIndex
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this DocumentIndex.


        :return: The id of this DocumentIndex.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentIndex.


        :param id: The id of this DocumentIndex.
        :type id: str
        """

        self._id = id

    @property
    def paragraphs(self):
        """Gets the paragraphs of this DocumentIndex.


        :return: The paragraphs of this DocumentIndex.
        :rtype: List[DocumentIndexParagraphs]
        """
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs):
        """Sets the paragraphs of this DocumentIndex.


        :param paragraphs: The paragraphs of this DocumentIndex.
        :type paragraphs: List[DocumentIndexParagraphs]
        """

        self._paragraphs = paragraphs

    @property
    def source(self):
        """Gets the source of this DocumentIndex.

        Source Document Record  # noqa: E501

        :return: The source of this DocumentIndex.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DocumentIndex.

        Source Document Record  # noqa: E501

        :param source: The source of this DocumentIndex.
        :type source: str
        """

        self._source = source