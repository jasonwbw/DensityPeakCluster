#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import math
import logging
import numpy as np

def load_paperdata(distance_f):
	distances = {}
	min_dis, max_dis = max_dis = sys.float_info.max, 0.0
	max_id = 0
	with open(distance_f, 'r') as fp:
		for line in fp:
			x1, x2, d = line.strip().split(' ')
			x1, x2 = int(x1), int(x2)
			max_id = max(max_id, x1, x2)
			dis = float(d)
			min_dis, max_dis = min(min_dis, dis), max(max_dis, dis)
			distances[(x1, x2)] = float(d)
			distances[(x2, x1)] = float(d)
	for i in xrange(max_id):
		distances[(i, i)] = 0.0
	return distances, max_dis, min_dis, max_id

def autoselect_dc(max_id, max_dis, min_dis, distances):
	percent = 2.0
	position = int(max_id * percent / 100)
	return sorted(distances.values())[position * 2 + max_id]

def local_density(max_id, distances, dc, guass=True, cutoff=False):
	assert guass and cutoff == False and guass or cutoff == True
	guass_func = lambda dij, dc : math.exp(- (dij / dc) ** 2)
	cutoff_func = lambda dij, dc: 1 if dij < dc else 0
	func = guass and guass_func or cutoff_func
	rho = [-1] + [0] * max_id
	for i in xrange(1, max_id):
		for j in xrange(i + 1, max_id + 1):
			rho[i] += func(distances[(i, j)], dc)
			rho[j] += func(distances[(i, j)], dc)
	return np.array(rho, np.float32)

def min_distance(max_id, distances, rho):
	sort_rho_idx = np.argsort(-rho)
	delta, nneigh = [0.0, -1.0] + [max(distances.values())] * (len(rho) - 2), [0] * len(rho)
	for i in xrange(1, max_id):
		for j in xrange(0, i):
			old_i, old_j = sort_rho_idx[i], sort_rho_idx[j]
			if distances[(old_i, old_j)] < delta[old_i]:
				delta[old_i] = distances[(old_i, old_j)]
				nneigh[old_i] = old_j
	return np.array(delta, np.float32), np.array(nneigh, np.float32)

class DensityPeakCluster(object):

	def cluster(self, load_func, distance_f, density_threshold, distance_threshold, dc = None):
		distances, max_dis, min_dis, max_id = load_func(distance_f)
		if dc == None:
			dc = autoselect_dc(max_id, max_dis, min_dis, distances)
		rho = local_density(max_id, distances, dc)
		delta, nneigh = min_distance(max_id, distances, rho)
		cluster, ccenter = {}, {}
		for idx, (ldensity, mdistance, nneigh_item) in enumerate(zip(rho, delta, nneigh)):
			if idx == 0: continue
			if ldensity >= density_threshold and mdistance >= distance_threshold:
				ccenter[idx] = idx
				cluster[idx] = idx
			elif nneigh_item in cluster:
				cluster[idx] = cluster[nneigh_item]
			else:
				cluster[idx] = -1
		self.cluster, self.ccenter = cluster, ccenter

if __name__ == '__main__':
	dpcluster = DensityPeakCluster()
	dpcluster.cluster(load_paperdata, './example_distances.dat', 1, 4)