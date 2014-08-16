#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import numpy as np
import matplotlib.pyplot as plt

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
	styles = ['k.', 'g.', 'r.', 'c.', 'm.', 'y.', 'b.']
	assert len(x) == len(y)
	if style_list != None:
		assert len(x) == len(style_list) and len(styles) >= len(set(style_list))
	plt.figure(which_fig)
	plt.clf()
	if style_list == None:
		plt.plot(x, y, styles[0])
	else:
		clses = set(style_list)
		xs, ys = {}, {}
		for i in xrange(len(x)):
			try:
				xs[style_list[i]].append(x[i])
				ys[style_list[i]].append(y[i])
			except KeyError:
				xs[style_list[i]] = [x[i]]
				ys[style_list[i]] = [y[i]]
		for idx, cls in enumerate(clses):
			if cls == -1:
				style = styles[0]
			else:
				style = styles[idx + 1]
			plt.plot(xs[cls], ys[cls], style)
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.ylim(bottom = 0)
	plt.show()

if __name__ == '__main__':
	x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 7, 7])
	y = np.array([2, 3, 4, 5, 6, 2, 4, 8, 5, 6])
	cls = np.array([1, 4, 2, 3, 5, -1, -1, 6, 6, 6])
	plot_scatter_diagram(0, x, y, style_list = cls)
