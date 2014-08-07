#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import numpy as np
from cluster import *
import matplotlib.pyplot as plt

def plot_scatter_diagram(which_fig, x, y, x_label = 'x', y_label = 'y', title = 'title'):
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
	plot_scatter_diagram(0, rho[1:], delta[1:], x_label='rho', y_label='delta', title='rho-delta')

if __name__ == '__main__':
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	dpcluster = DensityPeakCluster()
	rho, delta, nneigh = dpcluster.cluster(load_paperdata, './example_distances.dat', 20, 0.1)
	print len(dpcluster.ccenter), 'center as below'
	for idx, center in dpcluster.ccenter.items():
		print rho[center], delta[center]
	plot_rho_delta(rho, delta)