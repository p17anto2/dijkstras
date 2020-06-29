def path_find(network, s):
    d = [-1 for x in network.nodes]
    path = ["-" for x in network.nodes]
    d[s] = 0
    queue = list(range(len(network.nodes)))
    while len(queue) != 0:
        next_min = d[queue[0]]
        to_visit = queue[0]
        for node in queue:
            if d[node] < next_min and d[node] != -1:
                next_min = d[node]
                to_visit = node
        queue.remove(to_visit)
        visit(network, network.nodes[to_visit].pointer, d, path)
    return path


def visit(network, node, d, path):
    for neighbor in network.neighbor_list[node]:
        if d[neighbor] == -1:
            d[neighbor] = d[node] + network.nodes[node].neighbors[neighbor]
            path[neighbor] = node
        elif d[neighbor] > d[node] + network.nodes[node].neighbors[neighbor]:
            d[neighbor] = d[node] + network.nodes[node].neighbors[neighbor]
            path[neighbor] = node