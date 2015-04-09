__author__ = 'Archana V Menon, Sujith V'

from approximate_vertex_cover import approximate_vertex_cover_2

def seed():

    # get graph
    from read_graph import read_graph
    G = read_graph("data/CA-GrQc.txt")

    print "nodes", len(G.nodes())

    v=approximate_vertex_cover_2(G)
    v10=[]

    for i in range(0,10,1):
        v10.append(v[i])

    print v10

    current_infected_nodes = v10
    time = int(raw_input("Enter time elapsed : "))

    infected_nodes = []
    infected_nodes.extend(current_infected_nodes)



    for t in range(0, time):
        temp = []
        for x in current_infected_nodes:
            temp.extend(G.neighbors(x))
        current_infected_nodes = temp

        for x in temp :
            if not x in infected_nodes:
                infected_nodes.append(x)

        print "Time: ", t + 15
        #print "Infected nodes: ", infected_nodes
        print "Count: ", len(infected_nodes)

        print ""

    safe_nodes = G.nodes()
    for x in infected_nodes:
        safe_nodes.remove(x)

    print "Safe nodes : ", safe_nodes
    print "Infected nodes : ", infected_nodes


    # draw the graph
    #from draw_graph import draw_graph_1
    #draw_graph_1(G, safe_nodes, infected_nodes, G.edges(), None)


seed()



