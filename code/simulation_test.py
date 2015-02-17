__author__ = 'Archana V Menon, Sujith V'

import networkx as nx
import matplotlib.pyplot as plt

def process_graph(G):

    """
    This function processes a given graph.
    Reads initial infected nodes and time elapsed
    Generates a list of safe nodes and infected nodes after the given time interval

    :param G: networkx graph
    """

    current_infected_nodes =  (str(raw_input("Enter initial infected nodes : "))).split(' ')
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

    safe_nodes = G.nodes()
    for x in infected_nodes:
        safe_nodes.remove(x)

    print "Safe nodes : ", safe_nodes
    print "Infected nodes : ", infected_nodes

    draw_graph(G, safe_nodes, infected_nodes)



def draw_graph(G, safe_nodes, infected_nodes):

    """
    This function is used to draw status of a given graph

    :param G: given networkx graph
    :param safe_nodes: safe nodes list
    :param infected_nodes: infected nodes list
    """

    # positions for all nodes
    pos = nx.spring_layout(G)

    # safe nodes
    nx.draw_networkx_nodes(G, pos, nodelist=safe_nodes, node_size=30, node_color='y')

    # infected_nodes
    nx.draw_networkx_nodes(G, pos, nodelist=infected_nodes, node_size=50, node_color='r')

    # edges
    nx.draw_networkx_edges(G,pos, width=1)

    # labels for nodes
    # nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

    plt.show() # display



if __name__ == "__main__":

    # get graph
    from read_graph import read_graph
    G = read_graph("data/roadNet-CA.txt")

    # process graph
    process_graph(G)



