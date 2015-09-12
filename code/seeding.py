__author__ = 'Archana V Menon, Sujith V'

import networkx as nx
from approximate_dominating_set import dominating_set

def seed(G):

    current_infected_nodes = []

    disjoint_graphs = nx.connected_component_subgraphs(G)
    for cc in disjoint_graphs :
        ds = dominating_set(cc)
        current_infected_nodes.append(ds[0])

    number_of_initial_affected_nodes = len(current_infected_nodes)

    infected_nodes = []
    infected_nodes.extend(current_infected_nodes)

    x_cor = []
    y_cor = []
    x_cor.append(0)
    y_cor.append(len(infected_nodes))

    print "\nGraph details \n"
    print "Graph size : ", len(G)
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

    from draw_graph import draw_curve
    draw_curve(x_cor, y_cor)


if __name__ == '__main__' :
    # get graph
    from read_graph import read_graph
    G = read_graph("data/CA-GrQc.txt")

    seed(G)



