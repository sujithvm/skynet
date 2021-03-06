__author__ = 'Archana V Menon, Sujith V'

import networkx as nx
from approximate_dominating_set import dominating_set
from approximate_vertex_cover import vertex_cover

from random import choice

'''
type :
    1 - dominating set
    2 - vertex cover
    3 - pso
    4 - random
'''

def seed(G, type):

    current_infected_nodes = []

    disjoint_graphs_gen = nx.connected_component_subgraphs(G)
    disjoint_graphs = list(disjoint_graphs_gen)

    for cc in disjoint_graphs :
        if type == 1 :
            ds = dominating_set(cc)
            current_infected_nodes.append(ds[0])

        elif type == 2 :
            vc = vertex_cover(cc)
            current_infected_nodes.append(vc[0])

        elif type == 3 :
            rand_node = choice(cc.nodes())
            current_infected_nodes.append(rand_node)

    number_of_initial_affected_nodes = len(current_infected_nodes)

    infected_nodes = []
    infected_nodes.extend(current_infected_nodes)

    x_cor = []
    y_cor = []
    x_cor.append(0)
    y_cor.append(len(infected_nodes))

    print "\nGraph details \n"
    print "Graph size : ", len(G.nodes())
    print "Number of disjoint graphs : ", len(disjoint_graphs)
    print "Number of initial affected nodes : ", number_of_initial_affected_nodes
    print "Initial affected nodes : ", infected_nodes

    print ""
    print "Time", "\t", "Number of infected nodes"

    time = 0
    print time, "\t\t", len(infected_nodes)

    while len(infected_nodes) != len(G) :
        temp = set()
        for x in current_infected_nodes:
            temp = temp.union(set(G.neighbors(x)))
        current_infected_nodes = temp

        for x in temp :
            if not x in infected_nodes:
                infected_nodes.append(x)

        print time + 1, "\t\t", len(infected_nodes)

        x_cor.append(time + 1)
        y_cor.append(len(infected_nodes))

        time += 1

    safe_nodes = G.nodes()
    for x in infected_nodes:
        if (x in safe_nodes):
            safe_nodes.remove(x)

    # print "\nSafe nodes : ", safe_nodes
    # print "\nInfected nodes : ", infected_nodes

    # from draw_graph import draw_graph
    # draw_graph(G, nodes_list1=infected_nodes, nodes_list2=safe_nodes, edge_list1=G.edges(), edge_list2=None)


    return x_cor, y_cor




if __name__ == '__main__' :
    # get graph
    from read_graph import read_graph
    G = read_graph("data/CA-GrQc.txt")


    ds_x_cor, ds_y_cor = seed(G, 1)
    vc_x_cor, vc_y_cor = seed(G, 2)
    rand_x_cor, rand_y_cor = seed(G, 3)


    from draw_graph import draw_curve
    draw_curve(ds_x_cor, ds_y_cor, "Dominating set",
               vc_x_cor, vc_y_cor, "Vertex cover",
               rand_x_cor, rand_y_cor, "Random selection")

