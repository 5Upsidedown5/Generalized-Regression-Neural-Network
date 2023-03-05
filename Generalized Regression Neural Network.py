import math
import random

import numpy as np

def distance(size, diemension, input_x, checked_x):
    dist = np.zeros([size])
    for j in range(size):
        for i in range(diemension):
            dist[j] += math.pow((checked_x[i] - input_x[j, i]), 2)
        dist[j] = math.sqrt(dist[j])
    return dist

def sum(size, diemension, input_x, checked_x, sigma):
    output = np.zeros([size])
    dist = np.zeros([size])
    for j in range(size):
        dist = distance(size, diemension, input_x, checked_x)
        output[j] += math.exp(-1 * math.pow((dist[j] / sigma), 2))
    return output
if __name__ == '__main__':
    n = 4 #number of entrance
    dim = 3 #number of dimensions
    g = 0
    w = np.zeros([n])
    x = np.zeros([n, dim])
    checked_x = np.zeros([dim])
    sigma = 1
    numerator = 0
    denominator = 0
    for j in range(n):
        w[j] = random.randint(0, 10) * random.random()
        for i in range(dim):
            x[j, i] = random.randint(0, 10)
    for i in range(dim):
        checked_x[i] = random.randint(0, 10) * random.random()
    output = sum(n, dim, x, checked_x, sigma)
    for i in range(n):
        numerator += w[i] * output[i]
        denominator += output[i]
        g = numerator/denominator
    print(g)