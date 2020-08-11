# -*- coding: utf-8 -*-
""" run """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
import sys
import logging
from argparse import ArgumentParser

from cytomine import CytomineJob


def main():
    """
    Executes some code as a Cytomine Job

    Usage:
        # Execute run.py through your local python
        python run.py --cytomine_host 'localhost-core' --cytomine_public_key '9af03585-c162-464e-bbf9-9196ff084487' --cytomine_private_key 'fb14e576-c534-410d-8206-5e70b0d97d96' --cytomine_id_project 237 --cytomine_id_image_instance 1220 --cytomine_id_software 4882

        # Execute your image on your computer.
        # remember to first build your image: docker build -t cyto_soft-1 .
        docker run --gpus all -it --rm --network=host cyto_soft-1 --cytomine_host 'localhost-core' --cytomine_public_key '9af03585-c162-464e-bbf9-9196ff084487' --cytomine_private_key 'fb14e576-c534-410d-8206-5e70b0d97d96' --cytomine_id_project 237 --cytomine_id_image_instance 1220 --cytomine_id_software 4882

        # Execute your image on your computer sharing your project directory with your docker image
        # so all the changes, during development, can be tested without re-building the the image
        # remember to first build your image: docker build -t cyto_soft-1 .
        docker run --gpus all -it --rm --mount type=bind,source=/home/giussepi/Public/environments/cyto_soft-1/,target=/myapp,bind-propagation=private --network=host cyto_soft-1 --cytomine_host 'localhost-core' --cytomine_public_key '9af03585-c162-464e-bbf9-9196ff084487' --cytomine_private_key 'fb14e576-c534-410d-8206-5e70b0d97d96' --cytomine_id_project 237 --cytomine_id_image_instance 1220 --cytomine_id_software 4882
    """

    parser = ArgumentParser(prog="Cytomine Python client example")

    # Cytomine connection parameters
    parser.add_argument('--cytomine_host', dest='host',
                        default='demo.cytomine.be', help="The Cytomine host")
    parser.add_argument('--cytomine_public_key', dest='public_key',
                        help="The Cytomine public key")
    parser.add_argument('--cytomine_private_key', dest='private_key',
                        help="The Cytomine private key")
    parser.add_argument('--cytomine_id_project', dest='id_project',
                        help="The project from which we want the images")
    parser.add_argument('--cytomine_id_software', dest='id_software',
                        help="The software to be used to process the image")
    parser.add_argument('--cytomine_id_image_instance', dest='id_image_instance',
                        help="The image to which the annotations will be added")

    params, _ = parser.parse_known_args(sys.argv[1:])

    with CytomineJob.from_cli(sys.argv[1:]) as cytomine:
        # Place your processing operations here
        print("Parameters received:")
        print('host: {}'.format(params.host))
        print('public_key: {}'.format(params.public_key))
        print('private_key: {}'.format(params.private_key))
        print('id_project: {}'.format(params.id_project))
        print('id_software: {}'.format(params.id_software))
        print('id_image_instance: {}'.format(params.id_image_instance))
        cytomine.job.update(statusComment="Finished.")


if __name__ == "__main__":
    main()
