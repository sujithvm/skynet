__author__ = 'Archana V Menon, Sujith V'

import networkx as nx

def read_graph(file_path):

    """
    This function is used to read graph from a given input file

    :param file_path: path of file
    :return: returns a graph generated from the edges read from the file
    """

    edge_list = []

    # input file
    input_file = open(file_path)

    # process graph edges
    for line in input_file.readlines() :
        line = line.strip()

        # ignore lines starting with '#'
        if line.startswith('#') :
            continue

        edge = tuple(line.split('\t'))
        edge_list.append(edge)

    # make a new graph
    G = nx.Graph()

    # uncomment to add all egdes
    # G.add_edges_from(edge_list)

    # adding only 1st 1000 edges to graph for testing purpose only
    G.add_edges_from(edge_list)

    return G


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