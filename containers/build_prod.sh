#!/bin/bash
REGISTRY=localhost:32000
cd ..
docker build --pull --rm -f "containers/Dockerfile" -t $REGISTRY/textindexer:latest "."
docker push $REGISTRY/textindexer:latest
