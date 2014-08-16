#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
from plot import *
from cluster import *

def plot(data):
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	dpcluster = DensityPeakCluster()
	distances, max_dis, min_dis, max_id, rho = local_density(load_paperdata, data)
	delta, nneigh = min_distance(max_id, distances, rho)
	plot_rho_delta(rho, delta)   #plot to choose the threthold

if __name__ == '__main__':
	plot('./data/data_in_paper/example_distances.dat')
