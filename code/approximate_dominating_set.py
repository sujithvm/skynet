__author__ = 'Archana V Menon, Sujith V'

import networkx as nx

def min_edge_dominating_set(G):

    """
    Find minimum edge dominating set

    :param G: networkx graph
    :return: set of edges
    :raise ValueError: when graph is null
    """

    if not G:
        raise ValueError("Error : null graph")

    return nx.maximal_matching(G)


if __name__ == "__main__":

    # get graph
    from read_graph import read_graph
    G = read_graph("data/roadNet-CA.txt")

    # find approximate dominating set
    ds = min_edge_dominating_set(G)

    print ds