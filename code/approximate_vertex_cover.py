__author__ = 'Archana V Menon, Sujith V'

def vertex_cover(G):

    """
    Finds a 2-approximation for a minimal vertex cover of the specified
    graph. The algorithm promises a cover that is at most double the size
    of a minimal cover. The algorithm takes O(|E|) time.

    http://en.wikipedia.org/wiki/Vertex_cover

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

        # arbitrary edge of graph
        e = graph.edges_iter().next()

        # e = (u, v)
        u = e[0]
        v = e[1]

        # C = C union {u,v}
        vertex_cover.append(u)
        vertex_cover.append(v)

        # single node
        if u == v :
            graph.remove_node(u)
            continue

        # delete the nodes from graph
        graph.remove_node(u)
        graph.remove_node(v)


    # return vertex_cover
    return vertex_cover


if __name__ == "__main__":


    # get graph
    # from read_graph import read_graph
    # G = read_graph("data/CA-GrQc.txt")

    from test_graphs import test_graph2

    G = test_graph2()

    # find approximate vertex cover
    vc = vertex_cover(G)

    print "Approximate vertex cover \n"
    print "Graph size : ", len(G)
    print "Length     : ", len(vc)
    print "Nodes      : ", vc

    nodes_list1 = vc
    nodes_list2 = G.nodes()
    for node in nodes_list1:
        nodes_list2.remove(node)

    # draw graph
    print "\n\nDrawing graph. Might take some time ..."
    #from draw_graph import draw_graph
    #draw_graph(G, nodes_list1, nodes_list2, G.edges(), None)

    import networkx as nx
    nx.draw_graphviz(G)

