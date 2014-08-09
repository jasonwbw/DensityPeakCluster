#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import numpy as np
from cluster import *
from sklearn import manifold
from plot_utils import *

def plot_rho_delta(rho, delta):
	'''
	Plot scatter diagram for rho-delta points

	Args:
		rho   : rho list
		delta : delta list
	'''
	logger.info("PLOT: rho-delta plot")
	plot_scatter_diagram(0, rho[1:], delta[1:], x_label='rho', y_label='delta', title='rho-delta')

def plot_cluster(cluster):
	'''
	Plot scatter diagram for final points that using multi-dimensional scaling for data

	Args:
		cluster : DensityPeakCluster object
	'''
	logger.info("PLOT: cluster result, start multi-dimensional scaling")
	dp = np.zeros((cluster.max_id, cluster.max_id), dtype = np.float32)
	cls = []
	for i in xrange(1, cluster.max_id):
		for j in xrange(i + 1, cluster.max_id + 1):
			dp[i - 1, j - 1] = cluster.distances[(i, j)]
			dp[j - 1, i - 1] = cluster.distances[(i, j)]
		cls.append(cluster.cluster[i])
	cls.append(cluster.cluster[cluster.max_id])
	cls = np.array(cls, dtype = np.float32)																																																											
	seed = np.random.RandomState(seed=3)
	mds = manifold.MDS()
	dp_mds = mds.fit_transform(dp)
	logger.info("PLOT: end mds, start plot")
	plot_scatter_diagram(1, dp_mds[:, 0], dp_mds[:, 1], title='cluster', style_list = cls)

if __name__ == '__main__':
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	dpcluster = DensityPeakCluster()
	rho, delta, nneigh = dpcluster.cluster(load_paperdata, './example_distances.dat', 20, 0.1)
	logger.info(str(len(dpcluster.ccenter)) + ' center as below')
	for idx, center in dpcluster.ccenter.items():
		logger.info('%d %f %f' %(idx, rho[center], delta[center]))
	#plot_rho_delta(rho, delta)   #plot to choose the threthold
	plot_cluster(dpcluster)