from vec import Vec
from random import randrange
from operator import itemgetter

# The raw data points
raw_data = [
    (41, 45),(39, 44),(42, 43),(44, 43),(10, 42),(38, 42),
    (8, 41),(41, 41),(13, 40),(45, 40),(7, 39),(38, 39),
    (42, 39),(9, 38),(12, 38),(19, 38),(25, 38),(6, 37),
    (13, 35),(9, 34),(12, 34),(32, 27),(26, 25),(39, 24),
    (34, 23),(37, 23),(22, 22),(38, 21),(35, 20),(31, 18),
    (26, 16),(38, 13),(29, 11),(34, 11),(37, 10),(40, 9),(42, 9)
]

# Create vectors
data = [Vec(x, y) for x, y in raw_data]

# Find the min and max range of data-points
minX = min(raw_data, key=itemgetter(0))[0]
maxX = max(raw_data, key=itemgetter(0))[0]
minY = min(raw_data, key=itemgetter(1))[1]
maxY = max(raw_data, key=itemgetter(1))[1]

# Define the number of clusters
k = 4
# A dictionary of clusters
clusters = {}
# Count the number of iterations until convergence
iterations = 0
# Will be used to determine if the algorithm is complete
convergence = False
# Initialize the means to random points in the general range of our dataset
means = [Vec(randrange(minX, maxX), randrange(minY, maxY)) for x in range(k)]

while convergence is False:
    iterations += 1
    clusters = {i : [] for i in range(0,k)}
    for v in data:
        cluster = -1
        distance = float('inf')
        for i in range(len(means)):
            d = Vec.distance(v, means[i])
            if d < distance:
                distance = d
                cluster = i
        clusters[cluster].append(v)

    # Create a list to store the new means
    new_means = []        
    for key in clusters:
        # Sum the vectors in each cluster
        summed = Vec.zero()
        cluster = clusters[key]
        for v in cluster:
            summed += v
       
        # Find the mean of all the vectors in each cluster
        count = len(cluster)
        if count > 0:
            new_means.append(summed / Vec(count, count))
        else:
            new_means.append(means[key])
    
    # If the new means are the same as the old, the algorithm has converged
    convergence = means == new_means
    means = new_means

for k in clusters:
    print('Cluster %d' % (k+1))
    print(clusters[k])
print('Finished in %d iterations' % iterations)

from collections import deque
from matplotlib import pyplot as plt
from matplotlib import style

x = [v.x for v in data]
y = [v.y for v in data]
colors = deque(['c', 'm', 'y', 'g'])

for k in clusters:
    x = [v.x for v in clusters[k]]
    y = [v.y for v in clusters[k]]
    plt.scatter(x, y, color=colors[0])
    colors.rotate()

for mean in means:
    x = [v.x for v in means]
    y = [v.y for v in means]
    plt.scatter(x, y, color='r', s=32, alpha=0.1)

plt.title('K-means Clustering')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
