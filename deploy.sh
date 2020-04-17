#!/bin/sh 

IMAGE="batters21/devops-18pi-dumderedum" 
GIT_VERSION=$(git describe --always --abbrev --tags --long)

docker build -t ${IMAGE}:${GIT_VERSION} .
docker tag ${IMAGE}:${GIT_VERSION} ${IMAGE}:latest

echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
docker push ${IMAGE}:${GIT_VERSION}
docker logout 