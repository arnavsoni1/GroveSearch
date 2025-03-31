import grovesearch as gs
import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=1)
G.add_edge('A', 'C', weight=3)
terminals = ['A', 'B', 'C']
quantum_res = gs.solve_steiner_grover(G, terminals)
print(f"Edges: {quantum_res.x}")
print(f"Total weight: {quantum_res.fval}\n") 
