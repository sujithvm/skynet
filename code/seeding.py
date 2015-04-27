__author__ = 'Archana V Menon, Sujith V'

from approximate_vertex_cover import dominating_set

def seed():

    # get graph
    from read_graph import read_graph
    G = read_graph("data/CA-GrQc.txt")

    print "Number of nodes: ", len(G.nodes())

    v=dominating_set(G)
    v10=[]

    for i in range(0,10,1):
        v10.append(v[i])

    print "\nInitial 10 nodes selected from dominating set: ", v10

    current_infected_nodes = v10
    time = int(raw_input("\nEnter time elapsed : "))

    infected_nodes = []
    infected_nodes.extend(current_infected_nodes)

    print ""
    print "Time", "\t", "Number of infected nodes"

    for t in range(0, time):
        temp = set()
        for x in current_infected_nodes:
            temp = temp.union(set(G.neighbors(x)))
        current_infected_nodes = temp

        for x in temp :
            if not x in infected_nodes:
                infected_nodes.append(x)

        print t + 1, "\t\t", len(infected_nodes)


    safe_nodes = G.nodes()
    for x in infected_nodes:
        safe_nodes.remove(x)

    print "\nSafe nodes : ", safe_nodes
    print "\nInfected nodes : ", infected_nodes


    # draw the graph
    #from draw_graph import draw_graph_1
    #draw_graph_1(G, safe_nodes, infected_nodes, G.edges(), None)


seed()



