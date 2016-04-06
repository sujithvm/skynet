__author__ = 'Archana V Menon, Sujith V'

import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(G, nodes_list1, nodes_list2, edge_list1, edge_list2):

    """
    This function is used to draw graphs

    :param G: networkx graph
    :param nodes_list1: list of nodes
    :param nodes_list2: list of nodes
    :param edge_list1: list of edges
    :param edge_list2: list of edges
    """

    # positions for all nodes
    pos = nx.spring_layout(G)

    # draw set of nodes
    nx.draw_networkx_nodes(G, pos, nodelist=nodes_list1, node_size=30, node_color='r')

    # draw set of nodes
    nx.draw_networkx_nodes(G, pos, nodelist=nodes_list2, node_size=50, node_color='y')


    # draw set of edges
    nx.draw_networkx_edges(G,pos, edgelist=edge_list1, width=1, edge_color='b')

    # draw set of edges
    nx.draw_networkx_edges(G,pos, edgelist=edge_list2, width=1, edge_color='g')

    # labels for nodes
    # nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

    plt.show() # display


def draw_curve(x1, y1, lab_1, x2, y2, lab_2, x3, y3, lab_3):
    l1 = plt.plot(x1, y1, label=lab_1)
    l2 = plt.plot(x2, y2, label=lab_2)
    l3 = plt.plot(x3, y3, label=lab_3)

    plt.legend()

    plt.axis([0, 20, 0, 6000])
    plt.xlabel("time/iterations")
    plt.ylabel("Number of nodes infected")

    plt.show()
