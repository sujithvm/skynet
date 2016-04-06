__author__ = 'Archana V Menon, Sujith V'

import networkx as nx
from approximate_dominating_set import dominating_set
from approximate_vertex_cover import vertex_cover

from random import choice
from random import randint

from pso import pso

BENEFIT_LOWER = 30
BENEFIT_UPPER = 70
COST_LOWER = 20
COST_UPPER = 50

OPT_BENEFIT_LOWER = 50
OPT_BENEFIT_UPPER = 60
OPT_COST_LOWER = 20
OPT_COST_UPPER = 30

THRESHOLD_DIFF = 400

INITIAL_COST = 3 * COST_UPPER

USE_PSO = False

'''
type :
    1 - dominating set
    2 - vertex cover
    3 - pso
    4 - random
'''

pso_node_map = {}

D = 1
def opt_func(x):
    x1 = x[0]
    x2 = x[1]

    #return x2 - D * x1
    return x2 -  x1

lb = [OPT_BENEFIT_LOWER, OPT_COST_LOWER]
ub = [OPT_BENEFIT_UPPER, OPT_COST_UPPER]


def optimize(G, nodes) :

    nv = []
    for node in nodes :
        D = G.degree(node)
        val = -opt_func( [G.node[node]["benefit"], G.node[node]["cost"]] )

        #if val > pso_node_map[D] :
        #    nv.append([node, D])
        nv.append([node, D])

    # sort by degree
    nv.sort(key=lambda x: x[1], reverse=True)

    print nv

    print " "

    filtered_nodes = []
    cost = INITIAL_COST
    for entry in nv :
        node = entry[0]
        node_cost = G.node[node]["cost"]

        if cost - node_cost >= 0 :
            filtered_nodes.append(node)
            cost -= node_cost

    return filtered_nodes


def seed(G, type):

    current_infected_nodes = []

    if type == 1 :
        ds = dominating_set(G)
        if USE_PSO : current_infected_nodes.extend(optimize(G, ds))
        else : current_infected_nodes.append(ds[0])

    elif type == 2 :
        vc = vertex_cover(G)
        if USE_PSO : current_infected_nodes.extend(optimize(G, vc))
        else : current_infected_nodes.append(vc[0])

    elif type == 3 :
        rand_node = choice(G.nodes())
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
    G1 = read_graph("data/CA-GrQc.txt")

    G = max(nx.connected_component_subgraphs(G1), key=len)

    degrees = G.degree()
    max_deg = G.degree( max(degrees, key=degrees.get) )

    for d in xrange(1, max_deg + 1) :
        D = d
        xopt, fopt = pso(opt_func, lb, ub)

        pso_node_map[d] = -fopt
        print d



    for n in G.nodes() :
        G.node[n]['cost'] = randint(COST_LOWER, COST_UPPER)
        G.node[n]['benefit'] = randint(BENEFIT_LOWER, BENEFIT_UPPER)

    ds_x_cor, ds_y_cor = seed(G, 1)
    vc_x_cor, vc_y_cor = seed(G, 2)
    rand_x_cor, rand_y_cor = seed(G, 3)


    from draw_graph import draw_curve
    draw_curve(ds_x_cor, ds_y_cor, "Dominating set",
               vc_x_cor, vc_y_cor, "Vertex cover",
               rand_x_cor, rand_y_cor, "Random selection")

