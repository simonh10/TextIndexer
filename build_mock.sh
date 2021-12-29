#!/bin/bash
REGISTRY=localhost:32000
docker build --pull --rm -f "Dockerfile.mock" -t $REGISTRY/textindexer:mock "."
docker push $REGISTRY/textindexer:mock
