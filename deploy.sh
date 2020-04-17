#!/bin/sh

IMAGE="batters21/devops-18pi-dumderedum" 

docker build -t ${IMAGE}:${GIT_VERSION} .
docker tag ${IMAGE}:${GIT_VERSION} ${IMAGE}:latest