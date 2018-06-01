/* In this exercise, before you compute projections, you're going to practice working with one of NetworkX's disk I/O functions, read_edgelist(). read_edgelist() creates a graph from the edgelist file. The graph that you'll be working with is a bipartite graph describing the American Revolution. There are two node partitions - 'people' and 'clubs', and edges denote a person being a member of a club. */


# Import networkx
import networkx as nx

# Read in the data: g
G = nx.read_edgelist('american-revolution.edgelist')

# Assign nodes to 'clubs' or 'people' partitions
for n, d in G.nodes(data=True):
    if '.' in n:
        G.node[n]['bipartite'] = 'people'
    else:
        G.node[n]['bipartite'] = 'clubs'
        
# Print the edges of the graph
print(G.edges())
