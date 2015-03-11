__author__ = 'Archana V Menon, Sujith V'


def approximate_vertex_cover_1(G):

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

        # delete the nodes from graph
        graph.remove_node(u)
        graph.remove_node(v)


    # return vertex_cover
    return vertex_cover



def approximate_vertex_cover_2(G):

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
    from read_graph import read_graph
    G = read_graph("data/roadNet-CA.txt")

    # find approximate vertex cover
    vc1 = approximate_vertex_cover_1(G)
    vc2 = approximate_vertex_cover_2(G)

    print "Vertex cover algorithm 1 : "
    print "Size : ", len(vc1)
    print "nodes : ", vc1

    print "Vertex cover algorithm 2 : "
    print "Size : ", len(vc2)
    print "nodes : ", vc2

    # draw graph
    from draw_graph import draw_graph
    nodes_list1 = vc1
    nodes_list2 = G.nodes()
    for node in nodes_list1:
        nodes_list2.remove(node)
    draw_graph(G, nodes_list1, nodes_list2, G.edges(), None)

    nodes_list1 = vc2
    nodes_list2 = G.nodes()
    for node in nodes_list1:
        nodes_list2.remove(node)
    draw_graph(G, nodes_list1, nodes_list2, G.edges(), None)

