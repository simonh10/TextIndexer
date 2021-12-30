# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from textindexer.server.models.base_model_ import Model
from textindexer.server import util


class DocumentRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, location=None, encoding=None, language=None, title=None, author=None, id=None, text=None, status=None):  # noqa: E501
        """DocumentRecord - a model defined in OpenAPI

        :param location: The location of this DocumentRecord.  # noqa: E501
        :type location: str
        :param encoding: The encoding of this DocumentRecord.  # noqa: E501
        :type encoding: str
        :param language: The language of this DocumentRecord.  # noqa: E501
        :type language: str
        :param title: The title of this DocumentRecord.  # noqa: E501
        :type title: str
        :param author: The author of this DocumentRecord.  # noqa: E501
        :type author: str
        :param id: The id of this DocumentRecord.  # noqa: E501
        :type id: str
        :param text: The text of this DocumentRecord.  # noqa: E501
        :type text: str
        :param status: The status of this DocumentRecord.  # noqa: E501
        :type status: str
        """
        self.openapi_types = {
            'location': str,
            'encoding': str,
            'language': str,
            'title': str,
            'author': str,
            'id': str,
            'text': str,
            'status': str
        }

        self.attribute_map = {
            'location': 'location',
            'encoding': 'encoding',
            'language': 'language',
            'title': 'title',
            'author': 'author',
            'id': 'id',
            'text': 'text',
            'status': 'status'
        }

        self._location = location
        self._encoding = encoding
        self._language = language
        self._title = title
        self._author = author
        self._id = id
        self._text = text
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'DocumentRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DocumentRecord of this DocumentRecord.  # noqa: E501
        :rtype: DocumentRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self):
        """Gets the location of this DocumentRecord.


        :return: The location of this DocumentRecord.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DocumentRecord.


        :param location: The location of this DocumentRecord.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501
        if location is not None and len(location) < 1:
            raise ValueError("Invalid value for `location`, length must be greater than or equal to `1`")  # noqa: E501

        self._location = location

    @property
    def encoding(self):
        """Gets the encoding of this DocumentRecord.


        :return: The encoding of this DocumentRecord.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this DocumentRecord.


        :param encoding: The encoding of this DocumentRecord.
        :type encoding: str
        """
        if encoding is not None and len(encoding) < 1:
            raise ValueError("Invalid value for `encoding`, length must be greater than or equal to `1`")  # noqa: E501

        self._encoding = encoding

    @property
    def language(self):
        """Gets the language of this DocumentRecord.


        :return: The language of this DocumentRecord.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DocumentRecord.


        :param language: The language of this DocumentRecord.
        :type language: str
        """
        if language is not None and len(language) < 1:
            raise ValueError("Invalid value for `language`, length must be greater than or equal to `1`")  # noqa: E501

        self._language = language

    @property
    def title(self):
        """Gets the title of this DocumentRecord.


        :return: The title of this DocumentRecord.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DocumentRecord.


        :param title: The title of this DocumentRecord.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def author(self):
        """Gets the author of this DocumentRecord.


        :return: The author of this DocumentRecord.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this DocumentRecord.


        :param author: The author of this DocumentRecord.
        :type author: str
        """
        if author is not None and len(author) < 1:
            raise ValueError("Invalid value for `author`, length must be greater than or equal to `1`")  # noqa: E501

        self._author = author

    @property
    def id(self):
        """Gets the id of this DocumentRecord.


        :return: The id of this DocumentRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentRecord.


        :param id: The id of this DocumentRecord.
        :type id: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this DocumentRecord.


        :return: The text of this DocumentRecord.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this DocumentRecord.


        :param text: The text of this DocumentRecord.
        :type text: str
        """

        self._text = text

    @property
    def status(self):
        """Gets the status of this DocumentRecord.


        :return: The status of this DocumentRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DocumentRecord.


        :param status: The status of this DocumentRecord.
        :type status: str
        """
        allowed_values = ["pending", "retrieving", "processing", "indexed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status