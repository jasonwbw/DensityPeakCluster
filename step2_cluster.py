#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
from plot import *
from cluster import *

def plot(data, density_threshold, distance_threshold):
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	dpcluster = DensityPeakCluster()
	rho, delta, nneigh = dpcluster.cluster(load_paperdata, data, density_threshold, distance_threshold)
	logger.info(str(len(dpcluster.ccenter)) + ' center as below')
	for idx, center in dpcluster.ccenter.items():
		logger.info('%d %f %f' %(idx, rho[center], delta[center]))
	#plot_rho_delta(rho, delta)   #plot to choose the threthold
	plot_cluster(dpcluster)

if __name__ == '__main__':
	plot('./data/data_in_paper/example_distances.dat', 20, 0.1)
