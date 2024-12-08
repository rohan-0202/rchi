import numpy as np


class Path:
    def __init__(self, amounts, points):
        self.remaining = len(amounts)
        self.amounts = amounts
        self.points = points

    def value(self):
        numer = 1
        for i in self.amounts:
            numer *= i
        return ((numer ** (1 / self.remaining)) * self.points) / np.exp(self.remaining)


def pathSum(paths):
    sum = 0
    for i in paths:
        sum += i.value()
    return sum


def findPaths(n, paths):  # will find all paths of length n and append them to paths
    pass


def atkLoss(tiles):  # input would be current hand of 13 tiles
    paths = []
    n = 1
    while n < 5 and len(paths) != 0:
        findPaths(n, paths)

    return np.exp(-0.001 * pathSum(paths))
