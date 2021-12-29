#!/bin/bash

docker run --rm -v "${PWD}:/app" openapitools/openapi-generator-cli generate -i /app/reference/TextIndexer-v1.yaml -g python-flask -o /app --additional-properties=packageName=textindexer.server
sudo chown -R $USER .