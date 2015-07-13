__author__ = 'Archana V Menon, Sujith V'

from test_graphs import test_graph2
from approximate_dominating_set import dominating_set
from fibonacci import fibonacci

# get graph
G = test_graph2()

# find approximate vertex cover
vertex_cover = dominating_set(G)

# generate fibonacci series
fib = fibonacci(len(vertex_cover))

# visited
visited = {}

# spread list
spread_list = []

# fib  counter
ctr = 0


for node in vertex_cover :

    # find neighbours of each node
    neighbours = G.neighbors(node)

    # empty list to find final list
    neighbour_not_in_vertex_cover = [node]

    for neigh in neighbours:

        # for each neighbour which is not in vertex cover and not previously visited
        if neigh not in vertex_cover and neigh not in visited :

            # add to final list
            neighbour_not_in_vertex_cover.append(neigh)

            # set visited to true for that neigh(node)
            visited[neigh] = True

    # add ( fib, node, neighbours ) to final list
    spread_list.append((fib[ctr], node, neighbour_not_in_vertex_cover))

    # increment count
    ctr += 1

# print data
for entry in spread_list:
    print entry


# draw graph
# from draw_graph import draw_graph
# draw_graph(G, spread_list)

