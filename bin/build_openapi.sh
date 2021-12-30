#!/bin/bash

sudo docker run --rm -v "${PWD}:/app" openapitools/openapi-generator-cli generate -i /app/reference/TextIndexer-v1.yaml -g python-flask -o /app --additional-properties=packageName=textindexer.server
sudo chown -R $USER .
echo "" >> textindexer/server/controllers/default_controller.py
echo "" >> textindexer/server/controllers/default_controller.py
echo "from .default_controller_implementation import *" >> textindexer/server/controllers/default_controller.py
