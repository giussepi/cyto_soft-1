# -*- coding: utf-8 -*-
""" publish_descriptor_dev """

from cytomine import Cytomine
from cytomine.utilities.descriptor_reader import read_descriptor


with Cytomine("localhost-core", "<your public key>", "<your private key>") as c:
    software = read_descriptor("descriptor.json")
    print("Not executable software created with ID {}".format(software.id))
