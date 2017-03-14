#! /usr/bin/env python
#-*- coding: utf-8 -*-

from math import sqrt
from abc import ABCMeta, abstractmethod
from error_wrongvec import WrongVecError

import numpy as np
import numpy.linalg as linalg


class Distance():
    """
      abstract class, represent distance of two vector

      Attributes:
      """

    __metaclass__ = ABCMeta

    @abstractmethod
    def distance(self, vec1, vec2):
        """
        Compute distance of two vector(one line numpy array)
        if you use scipy to store the sparse matrix, please use s.getrow(line_num).toarray() build the one dimensional array

        Args:
            vec1: the first line vector, an instance of array
            vec2: the second line vector, an instance of array

        Returns:
            the computed distance

        Raises:
            TypeError: if vec1 or vec2 is not numpy.ndarray and one line array
        """
        if not isinstance(vec1, np.ndarray) or not isinstance(vec2, np.ndarray):
            raise TypeError("type of vec1 or vec2 is not numpy.ndarray")
        if vec1.ndim is not 1 or vec2.ndim is not 1:
            raise WrongVecError("vec1 or vec2 is not one line array")
        if vec1.size != vec2.size:
            raise WrongVecError("vec1 or vec2 is not same size")
        pass
# end Distance


class PearsonDistance(Distance):
    """
    pearson distance

    a sub class of Distance
    """

    def distance(self, vec1, vec2):
        """
        Compute distance of two vector by pearson distance
        """
        super(PearsonDistance, self).distance(vec1, vec2)  # super method
        avg1, avg2 = (self._avg(vec1), self._avg(vec2))
        v1, v2 = ([item - avg1 for item in vec1[0]],
                  [item - avg1 for item in vec2[0]])
        sqrt1, sqrt2 = (sqrt(sum([pow(item, 2) for item in v1])), sqrt(
            sum([pow(item, 2) for item in v2])))
        if sqrt1 * sqrt2 == 0:
            return 1
        return - reduce(lambda n, m: n + m, [i * j for i, j in zip(v1, v2)]) \
            / (sqrt1 * sqrt2)

    def _avg(self, vec):
        """
        Compute average of a vector, just compute non-zero numbers

        Args:
            vec: a line vector, an instance of array

        Returns:
            the average of the vector
        """
        size = 0.0
        for i in vec[0]:
            if i != 0:
                size += 1
        if size == 0:
            return 0
        return vec.sum() / size
# end PearsonDistance


class ConsineDistance(Distance):
    """
    consine distance

    a sub class of Distance
    """

    def distance(self, vec1, vec2):
        """
        Compute distance of two vector by consine distance
        """
        super(ConsineDistance, self).distance(vec1, vec2)  # super method
        num = np.dot(vec1, vec2)
        denom = linalg.norm(vec1) * linalg.norm(vec2)
        if num == 0:
            return 1
        return - num / denom
# end ConsineDistance
