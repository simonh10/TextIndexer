#!/bin/bash
REGISTRY=localhost:32000
cd ..
docker build --pull --rm -f "containers/Dockerfile.mock" -t $REGISTRY/textindexer:mock "."
docker push $REGISTRY/textindexer:mock
