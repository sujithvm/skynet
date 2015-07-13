__author__ = 'Archana V Menon, Sujith V'

import networkx as nx

def test_graph1() :
    edge_list = [(1, 2),
                 (2, 3),
                 (3, 4),
                 (4, 1)]

    # edge_list = [(0, 1),
    #              (1, 2),
    #              (2, 3),
    #              (3, 0)]
    #

    G = nx.Graph()
    G.add_edges_from(edge_list)

    return G


def test_graph2() :
    edge_list = [(1, 2),
                 (1, 3),
                 (2, 4),
                 (3, 4),
                 (4, 5),
                 (4, 7),
                 (4, 8),
                 (5, 6),
                 (6, 7),
                 (8, 9),
                 (8, 10) ]

    # edge_list = [(0, 1),
    #              (0, 2),
    #              (1, 3),
    #              (2, 3),
    #              (3, 4),
    #              (3, 6),
    #              (3, 7),
    #              (4, 5),
    #              (5, 6),
    #              (7, 8),
    #              (7, 9) ]

    G = nx.Graph()
    G.add_edges_from(edge_list)

    return G