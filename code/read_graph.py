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
    G.add_edges_from(edge_list)

    return G