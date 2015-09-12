__author__ = 'Archana V Menon, Sujith V'


def dominating_set(G):

    """
    Finds a greedy approximation for a minimal vertex cover of a specified
    graph. At each iteration, the algorithm picks the vertex with the
    highest degree and adds it to the cover, until all edges are covered.

    :param G: networkx graph
    :return: vertex cover as a list of nodes
    :raise ValueError: when graph is null
    """

    if not G:
        raise ValueError("Error : null graph")

    # copy given graph
    graph = G.copy()

    # vertex cover list
    vertex_cover = []


    while len(graph.edges()) > 0 :

        # get degrees of all nodes in the graph
        deg = graph.degree()

        # find node with maximum degree
        v = max(deg, key=deg.get)

        # add the node to vertex cover
        vertex_cover.append(v)

        # delete the node from graph
        graph.remove_node(v)


    # return vertex_cover
    return vertex_cover



if __name__ == "__main__":

    # get graph
    # from read_graph import read_graph
    # G = read_graph("data/CA-GrQc.txt")

    from test_graphs import test_graph2

    G = test_graph2()

    # find approximate dominating set
    ds = dominating_set(G)

    print "Minimum dominating set \n"
    print "Graph size : ", len(G)
    print "Length     : ", len(ds)
    print "Nodes      : ", ds

    nodes_list1 = ds
    nodes_list2 = G.nodes()
    for node in nodes_list1:
        nodes_list2.remove(node)

    # draw graph
    print "\n\nDrawing graph. Might take some time ..."
    from draw_graph import draw_graph
    draw_graph(G, nodes_list1, nodes_list2, G.edges(), None)