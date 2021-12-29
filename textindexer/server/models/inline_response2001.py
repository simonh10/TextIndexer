# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from textindexer.server.models.base_model_ import Model
from textindexer.server.models.word import Word
from textindexer.server import util

from textindexer.server.models.word import Word  # noqa: E501

class InlineResponse2001(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count=None, word=None):  # noqa: E501
        """InlineResponse2001 - a model defined in OpenAPI

        :param count: The count of this InlineResponse2001.  # noqa: E501
        :type count: int
        :param word: The word of this InlineResponse2001.  # noqa: E501
        :type word: List[Word]
        """
        self.openapi_types = {
            'count': int,
            'word': List[Word]
        }

        self.attribute_map = {
            'count': 'count',
            'word': 'word'
        }

        self._count = count
        self._word = word

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this InlineResponse2001.


        :return: The count of this InlineResponse2001.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineResponse2001.


        :param count: The count of this InlineResponse2001.
        :type count: int
        """

        self._count = count

    @property
    def word(self):
        """Gets the word of this InlineResponse2001.


        :return: The word of this InlineResponse2001.
        :rtype: List[Word]
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this InlineResponse2001.


        :param word: The word of this InlineResponse2001.
        :type word: List[Word]
        """

        self._word = word