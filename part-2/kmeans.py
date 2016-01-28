from random import randrange
from operator import itemgetter
import numpy as np
import sys

# Load data from disk and create vectors
data = []
data_file = sys.argv[1]
lines = [
    line.strip('\n') for line in open(data_file) if '#' not in line
]

# Find the min and max values on both axis
maxX = -float('inf')
maxY = -float('inf')
minX = float('inf')
minY = float('inf')
for line in lines:
    parts = line.split()
    if len(parts) == 2:
        x = float(parts[0])
        y = float(parts[1])
        minX = min(x, minX)
        minY = min(y, minY)
        maxX = max(x, maxX)
        maxY = max(y, maxY)
        data.append(np.array([x, y]))

# Define the number of clusters
k = 4
# A dictionary of clusters
clusters = {}
# Count the number of iterations until convergence
iterations = 0
# Will be used to determine if the algorithm is complete
convergence = False
# Initialize the means to random points in the general range of our dataset
means = [np.array([randrange(minX, maxX), randrange(minY, maxY)]) for x in range(k)]

while convergence is False:
    iterations += 1
    clusters = {i : [] for i in range(0,k)}
    for v in data:
        cluster = -1
        distance = float('inf')
        for i in range(len(means)):
            d = np.linalg.norm(v - means[i])
            if d < distance:
                distance = d
                cluster = i
        clusters[cluster].append(v)
    # Create a list to store the new means
    new_means = []        
    for key in clusters:
        # Sum the vectors in each cluster
        summed = np.array([0, 0])
        cluster = clusters[key]
        for v in cluster:
            summed += v
       
        # Find the mean of all the vectors in each cluster
        count = len(cluster)
        if count > 0:
            new_means.append(summed / np.array([count, count]))
        else:
            new_means.append(means[key])
    
    # If the new means are the same as the old, the algorithm has converged
    convergence = np.array_equal(means, new_means)
    means = new_means

# Create a simple visualization using Matplotlib
from collections import deque
from matplotlib import pyplot as plt
from matplotlib import style

x = [data[0] for v in data]
y = [data[1] for v in data]
colors = deque(['b', 'r', 'w', 'k', 'c', 'm', 'y', 'g', 'orange', 'brown'])

for k in clusters:
    x = [v[0] for v in clusters[k]]
    y = [v[1] for v in clusters[k]]
    plt.scatter(x, y, color=colors[0])
    colors.rotate()

for mean in means:
    x = [v[0] for v in means]
    y = [v[1] for v in means]
    plt.scatter(x, y, color='r', s=32, alpha=0.3)

plt.title('K-means Clustering : %d Iterations' % (iterations))
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
