from network import *
from time import time
from matplotlib import pyplot as plt
import dijkstra_matrix
import dijkstra_list
import path_find

with open("coordinates.csv", "r") as cords:
    lines = cords.readlines()
coordinates = []
lines = [line.strip() for line in lines]
for line in lines:
    if line != 'x,y':
        single_cords = line.split(',')
        coordinates.append((single_cords[0], single_cords[1]))
cases = [coordinates[:50], coordinates[50:90], coordinates[90:120], coordinates[120:140], coordinates[140:]]
nodes = []
configs = [20, 25, 30, 20, 25]
times = []
times2 = []
paths = []
for case, config in zip(cases, configs):
    for cords in case:
        nodes.append(Node(float(cords[0]), float(cords[1]), case.index(cords)))
    caseNetwork = Network(nodes, config)
    costs = []
    start = time()
    for s in range(len(caseNetwork.nodes)):
        dijkstra_matrix.dijkstra_matrix(caseNetwork, s)
    end = time()
    delta = end - start
    times.append(delta)
    start2 = time()
    for s in range(len(caseNetwork.nodes)):
        dijkstra_list.dijkstra_list(caseNetwork, s)
    end2 = time()
    delta2 = end2 - start2
    times2.append(delta2)
    if case == cases[4]:
        for s in range(len(caseNetwork.nodes)):
            paths.append(str(path_find.path_find(caseNetwork, s)))
        with open("paths.txt", "w") as out:
            out.write("\n".join(paths))
    nodes.clear()
times.reverse()
times2.reverse()
x = [len(i) for i in cases]
x.reverse()
print(times)
print(x)
plt.plot([n for n in x], [x for x in times])
plt.plot([n for n in x], [x for x in times2])
plt.xlabel("Nodes")
plt.ylabel("Time")
plt.title("Dijkstra Time")
plt.legend(['Adjacency Matrix', 'Neighbor List'])
plt.show()
