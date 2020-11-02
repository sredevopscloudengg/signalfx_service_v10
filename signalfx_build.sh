#!/bin/sh

# signalfx image name
IMAGE_NAME="signalfx"

# build the image for signalfx service
signalfx_build_image () {
    docker build -t $IMAGE_NAME:latest .
}

# create and start the container for signalfx service
signalfx_create_start_container () {
    # append winpty for non-linux env
    winpty docker run -p 4996:4996 -d $IMAGE_NAME
    
    # use the following command for linux env
    # docker run -p 4996:4996 -d $IMAGE_NAME
}

# run funcs
signalfx_build_image
signalfx_create_start_container