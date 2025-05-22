@echo off
REM Output executed commands and stop on errors.
setlocal EnableDelayedExpansion
set -e
echo Starting build process...

REM Uncomment the following line should the edge gateway have been given a different IP address.
REM docker buildx rm secure-edge-pro

REM Remove the existing instance if necessary
docker buildx rm secure-edge-pro || echo Instance does not exist or already removed

REM Create and initialize the build environment.
docker buildx create --name secure-edge-pro --config buildkitd-secure-edge-pro.toml
docker buildx use secure-edge-pro


REM Navigate to the tensor-flow-lite directory and build the tensor-flow-lite image with no cache
cd tensor-flow-lite
docker buildx build --platform linux/arm64/v8 --tag 192.168.140.1:5000/tensor-flow-lite:latest --no-cache --push .
cd ..

REM Navigate to the node-red directory and build the node-red image
cd node-red
docker buildx build --platform linux/arm64/v8 --tag 192.168.140.1:5000/node-red:latest --push .
cd ..


echo Build process completed.
endlocal
