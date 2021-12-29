# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from textindexer.server.models.document import Document  # noqa: E501
from textindexer.server.models.inline_response200 import InlineResponse200  # noqa: E501
from textindexer.server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from textindexer.server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_indexer_v1_document(self):
        """Test case for get_indexer_v1_document

        Your GET endpoint
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/indexer/v1/document',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_indexer_v1_document_doc_id(self):
        """Test case for get_indexer_v1_document_doc_id

        Your GET endpoint
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/indexer/v1/document/{doc_id}'.format(doc_id='doc_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_indexer_v1_document_doc_id_raw(self):
        """Test case for get_indexer_v1_document_doc_id_raw

        Your GET endpoint
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/indexer/v1/document/{doc_id}/raw'.format(doc_id='doc_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_indexer_v1_words(self):
        """Test case for get_indexer_v1_words

        Your GET endpoint
        """
        query_string = [('skip', 56),
                        ('limit', 56),
                        ('reverse', True)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/indexer/v1/words',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("text/plain not supported by Connexion")
    def test_post_indexer_v1_document(self):
        """Test case for post_indexer_v1_document

        
        """
        body = string
        query_string = [('filename', 'filename_example'),
                        ('encoding', 'encoding_example'),
                        ('language', 'language_example')]
        headers = { 
            'Content-Type': 'text/plain',
        }
        response = self.client.open(
            '/indexer/v1/document',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='text/plain',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
