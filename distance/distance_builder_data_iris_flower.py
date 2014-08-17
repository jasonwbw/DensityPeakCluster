#! /usr/bin/env python
#-*- coding: utf-8 -*-
#
# data reference : R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems"

from distance_builder import *
from distance import *

import numpy as np

if __name__ == '__main__':
  builder = DistanceBuilder()
  builder.load_points(r'../data/data_iris_flower/iris.data')
  builder.build_distance_file_for_cluster(ConsineDistance(), r'../data/data_iris_flower/iris.forcluster')