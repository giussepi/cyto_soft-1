#!/bin/bash
#
# Use this script to test locally the algorithm implementation, with default values for not Cytomine-related parameters.
#
# Example:
#     bash test.sh localhost-core 9af03585-c162-464e-bbf9-9196ff084487 fb14e576-c534-410d-8206-5e70b0d97d96 237 1220 4882


CYTOMINE_HOST=$1
CYTOMINE_PUBLIC_KEY=$2
CYTOMINE_PRIVATE_KEY=$3
CYTOMINE_ID_PROJECT=$4
CYTOMINE_ID_IMAGE=$5
CYTOMINE_ID_SOFTWARE=$6


IMAGE="cyto_soft-1"

ADD_HOST=""
if [[ $CYTOMINE_HOST = *"localhost"* ]];
then
    ADD_HOST="--add-host=${CYTOMINE_HOST}:172.17.0.1"
fi

docker build -t $IMAGE .
docker run $ADD_HOST -it $IMAGE --cytomine_host $CYTOMINE_HOST \
   --cytomine_public_key $CYTOMINE_PUBLIC_KEY \
   --cytomine_private_key $CYTOMINE_PRIVATE_KEY \
   --cytomine_id_project $CYTOMINE_ID_PROJECT \
   --cytomine_id_image_instance $CYTOMINE_ID_IMAGE \
   --cytomine_id_software $CYTOMINE_ID_SOFTWARE
