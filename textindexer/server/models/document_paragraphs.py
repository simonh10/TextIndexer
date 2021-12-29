# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from textindexer.server.models.base_model_ import Model
from textindexer.server.models.document_sentences import DocumentSentences
from textindexer.server import util

from textindexer.server.models.document_sentences import DocumentSentences  # noqa: E501

class DocumentParagraphs(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, index=None, sentences=None):  # noqa: E501
        """DocumentParagraphs - a model defined in OpenAPI

        :param index: The index of this DocumentParagraphs.  # noqa: E501
        :type index: int
        :param sentences: The sentences of this DocumentParagraphs.  # noqa: E501
        :type sentences: List[DocumentSentences]
        """
        self.openapi_types = {
            'index': int,
            'sentences': List[DocumentSentences]
        }

        self.attribute_map = {
            'index': 'index',
            'sentences': 'sentences'
        }

        self._index = index
        self._sentences = sentences

    @classmethod
    def from_dict(cls, dikt) -> 'DocumentParagraphs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Document_paragraphs of this DocumentParagraphs.  # noqa: E501
        :rtype: DocumentParagraphs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def index(self):
        """Gets the index of this DocumentParagraphs.


        :return: The index of this DocumentParagraphs.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DocumentParagraphs.


        :param index: The index of this DocumentParagraphs.
        :type index: int
        """

        self._index = index

    @property
    def sentences(self):
        """Gets the sentences of this DocumentParagraphs.


        :return: The sentences of this DocumentParagraphs.
        :rtype: List[DocumentSentences]
        """
        return self._sentences

    @sentences.setter
    def sentences(self, sentences):
        """Sets the sentences of this DocumentParagraphs.


        :param sentences: The sentences of this DocumentParagraphs.
        :type sentences: List[DocumentSentences]
        """

        self._sentences = sentences
