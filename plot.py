#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import numpy as np
from cluster import *
import matplotlib.pyplot as plt
from sklearn import manifold

def plot_scatter_diagram(which_fig, x, y, x_label = 'x', y_label = 'y', title = 'title', style_list = None):
	'''
	Plot scatter diagram

	Args:
		which_fig  : which sub plot
		x          : x array
		y          : y array
		x_label    : label of x pixel
		y_label    : label of y pixel
		title      : title of the plot
	'''
	styles = ['b.', 'g.', 'r.', 'c.', 'm.', 'y.', 'k.', 'w.']
	plt.figure(which_fig)
	plt.clf()
	plt.plot(x, y, styles[0])
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.ylim(bottom = 0)
	plt.show()

def plot_rho_delta(rho, delta):
	logger.info("PLOT: rho-delta plot")
	plot_scatter_diagram(0, rho[1:], delta[1:], x_label='rho', y_label='delta', title='rho-delta')

def plot_cluster(cluster):
	logger.info("PLOT: cluster result, start multi-dimensional scaling")
	dp = np.zeros((cluster.max_id, cluster.max_id), dtype = np.float32)
	cls = []
	for i in xrange(1, cluster.max_id):
		for j in xrange(i + 1, cluster.max_id + 1):
			dp[i - 1, j - 1] = cluster.distances[(i, j)]
			dp[j - 1, i - 1] = cluster.distances[(i, j)]
		cls.append(cluster.cluster[i])
	cls.append(cluster.cluster[cluster.max_id])
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
	#plot_rho_delta(rho, delta)
	plot_cluster(dpcluster)