#!/bin/bash

# Output executed commands and stop on errors.
set -e -x

# Uncomment the following line should the edge gateway have been
# given a different IP address.
# docker buildx rm secure-edge-pro;

# Remove the existing instance if necessary
docker buildx rm secure-edge-pro || true

# Create and initialize the build environment.
docker buildx create --name secure-edge-pro \
                     --config buildkitd-secure-edge-pro.toml
docker buildx use secure-edge-pro

# Navigate to the tensor-flow-lite directory and build the influxdb image
cd tensor-flow-lite/
docker buildx build --platform linux/arm64/v8 --tag 192.168.140.1:5000/tensor-flow-lite:latest --push .
cd ..

# Navigate to the node-red directory and build the node-red image
cd node-red/
docker buildx build --platform linux/arm64/v8 --tag 192.168.140.1:5000/node-red:latest --push .
cd ..
