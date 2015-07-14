__author__ = 'Archana V Menon, Sujith V'

import networkx as nx

from read_graph import read_graph
G = read_graph("data/CA-GrQc.txt")

print "Connected components\n"

i = 1
disjoint_graphs = nx.connected_component_subgraphs(G)
for cc in disjoint_graphs :
    print "Graph ", i, " size : ", len(cc)
    i += 1

