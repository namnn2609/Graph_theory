import os
import copy
import numpy as np
from Graph_tool import multigraph as mg;
from Graph_tool import direct_multigraph as dmg;

# Wecome !
# This file we read and write some component of graph: node, arc, adjMatrix, Incidence matrix.
Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph' # This direction which you must be config.
Graph_1_1_dir=os.path.join(Graph_dir,'Graph_1_1')
Graph_1_5_dir=os.path.join(Graph_dir,'Graph_1_5')
Graph_1_12_dir=os.path.join(Graph_dir,'Graph_1_12')
Graph_1_13_dir=os.path.join(Graph_dir,'Graph_1_13')
Graph_1_18_dir=os.path.join(Graph_dir,'Graph_1_18')
Graph_1_29_dir=os.path.join(Graph_dir,'Graph_1_29')
Graph_3_3_dir=os.path.join(Graph_dir,'Graph_3_3')
# #Read graph from file
# G_11=dmg(5,10)
# G_11.read_nodes(os.path.join(Graph_1_1_dir,'nodes.txt'))
# G_11.read_arcs(os.path.join(Graph_1_1_dir,'arcs.txt'))
# G_11.read_adjMatrix(os.path.join(Graph_1_1_dir,'adjMatrix.txt'))
# G_11.read_inInMatrix(os.path.join(Graph_1_1_dir,'inInMatrix.txt'))
# G_11.read_outInMatrix(os.path.join(Graph_1_1_dir,'outInMatrix.txt'))
# print('Dãy bậc ra của đồ thị G_11:',end =" ")
# for i in G_11.Nodes:
#     if i != G_11.Nodes[-1]  : 
#         print(G_11.deg_out(i),'->', end =" ")
#     else:
#         print(G_11.deg_out(i))

# print('Dãy bậc vào của đồ thị G_11:',end =" ")
# for i in G_11.Nodes:
#     if i != G_11.Nodes[-1]  : 
#         print(G_11.deg_in(i),'->', end =" ")
#     else:
#         print(G_11.deg_in(i))

# G_11.SCC()
# #Display  Graphs
# G_11.display_node()
# G_11.display_arc()
# G_11.display_adjMatrix()
# G_11.display_inInMatrix()
# G_11.display_outInMatrix()

#Read graph 1.12 from file
G_12=dmg(6,8)
G_12.read_nodes(os.path.join(Graph_1_12_dir,'nodes.txt'))
G_12.read_arcs(os.path.join(Graph_1_12_dir,'arcs.txt'))
G_12.read_adjMatrix(os.path.join(Graph_1_12_dir,'adjMatrix.txt'))
G_12.read_inInMatrix(os.path.join(Graph_1_12_dir,'inInMatrix.txt'))
G_12.read_outInMatrix(os.path.join(Graph_1_12_dir,'outInMatrix.txt'))
#Display  Graphs
# print('Dãy bậc ra của đồ thị G_12:',end =" ")
# for i in G_12.Nodes:
#     if i != G_12.Nodes[-1]  : 
#         print(G_12.deg_out(i),'->', end =" ")
#     else:
#         print(G_12.deg_out(i))

# print('Dãy bậc vào của đồ thị G_12:',end =" ")
# for i in G_12.Nodes:
#     if i != G_12.Nodes[-1]  : 
#         print(G_12.deg_in(i),'->', end =" ")
#     else:
#         print(G_12.deg_in(i))
# G_12.SCC()
# G_12.display_node()
# G_12.display_arc()
# G_12.display_adjMatrix()
# G_12.display_inInMatrix()
# G_12.display_outInMatrix()

#Read graph 1.13 from file
G_13=dmg(9,19)
G_13.read_nodes(os.path.join(Graph_1_13_dir,'nodes.txt'))
G_13.read_arcs(os.path.join(Graph_1_13_dir,'arcs.txt'))
G_13.read_adjMatrix(os.path.join(Graph_1_13_dir,'adjMatrix.txt'))
G_13.read_inInMatrix(os.path.join(Graph_1_13_dir,'inInMatrix.txt'))
G_13.read_outInMatrix(os.path.join(Graph_1_13_dir,'outInMatrix.txt'))
# #Display  Graphs
# print('Dãy bậc ra của đồ thị G_13:',end =" ")
# for i in G_13.Nodes:
#     if i != G_13.Nodes[-1]  : 
#         print(G_13.deg_out(i),'->', end =" ")
#     else:
#         print(G_13.deg_out(i))

# print('Dãy bậc vào của đồ thị G_13:',end =" ")
# for i in G_13.Nodes:
#     if i != G_13.Nodes[-1]  : 
#         print(G_13.deg_in(i),'->', end =" ")
#     else:
#         print(G_13.deg_in(i))
# G_13.SCC()
# G_13.display_node()
# G_13.display_arc()
# G_13.display_adjMatrix()
# G_13.display_inInMatrix()
# G_13.display_outInMatrix()


G_18=dmg(6,9)
G_18.read_nodes(os.path.join(Graph_1_18_dir,'nodes.txt'))
G_18.read_arcs(os.path.join(Graph_1_18_dir,'arcs.txt'))
G_18.read_adjMatrix(os.path.join(Graph_1_18_dir,'adjMatrix.txt'))
G_18.read_inInMatrix(os.path.join(Graph_1_18_dir,'inInMatrix.txt'))
G_18.read_outInMatrix(os.path.join(Graph_1_18_dir,'outInMatrix.txt'))
#Display  Graphs
# print('Dãy bậc ra của đồ thị G_18:',end =" ")
# for i in G_18.Nodes:
#     if i != G_18.Nodes[-1]  : 
#         print(G_18.deg_out(i),'->', end =" ")
#     else:
#         print(G_18.deg_out(i))

# print('Dãy bậc vào của đồ thị G_18:',end =" ")
# for i in G_18.Nodes:
#     if i != G_18.Nodes[-1]  : 
#         print(G_18.deg_in(i),'->', end =" ")
#     else:
#         print(G_18.deg_in(i))
# G_18.SCC()
# G_18.display_node()
# G_18.display_arc()
# G_18.display_adjMatrix()
# G_18.display_inInMatrix()
# G_18.display_outInMatrix()

G_29=dmg(6,6)
G_29.read_nodes(os.path.join(Graph_1_29_dir,'nodes.txt'))
G_29.read_arcs(os.path.join(Graph_1_29_dir,'arcs.txt'))
G_29.read_adjMatrix(os.path.join(Graph_1_29_dir,'adjMatrix.txt'))
G_29.read_inInMatrix(os.path.join(Graph_1_29_dir,'inInMatrix.txt'))
G_29.read_outInMatrix(os.path.join(Graph_1_29_dir,'outInMatrix.txt'))

# print('Dãy bậc ra của đồ thị G_29:',end =" ")
# for i in G_29.Nodes:
#     if i != G_29.Nodes[-1]  : 
#         print(G_29.deg_out(i),'->', end =" ")
#     else:
#         print(G_29.deg_out(i))

# print('Dãy bậc vào của đồ thị G_29:',end =" ")
# for i in G_29.Nodes:
#     if i != G_29.Nodes[-1]  : 
#         print(G_29.deg_in(i),'->', end =" ")
#     else:
#         print(G_29.deg_in(i))
# G_29.SCC()
# #Display  Graphs
# G_29.display_node()
# G_29.display_arc()
# G_29.display_adjMatrix()
# G_29.display_inInMatrix()
# G_29.display_outInMatrix()

G_33=mg(12,11)

Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'
Graph_3_3_dir=os.path.join(Graph_dir,'Graph_3_3')

G_33.read_vertex(os.path.join(Graph_3_3_dir,'vertex.txt'))
G_33.read_edges(os.path.join(Graph_3_3_dir,'edges.txt'))
G_33.read_adjMatrix(os.path.join(Graph_3_3_dir,'adjMatrix.txt'))
G_33.read_InMatrix(os.path.join(Graph_3_3_dir,'InMatrix.txt'))

# G_33.display_vertex()
# G_33.display_edge()
# G_33.display_adjMatrix()
# G_33.display_inMatrix()


G_15=dmg(4,8)
G_15.read_nodes(os.path.join(Graph_1_5_dir,'nodes.txt'))
G_15.read_arcs(os.path.join(Graph_1_5_dir,'arcs.txt'))
G_15.read_adjMatrix(os.path.join(Graph_1_5_dir,'adjMatrix.txt'))
G_15.read_inInMatrix(os.path.join(Graph_1_5_dir,'inInMatrix.txt'))
G_15.read_outInMatrix(os.path.join(Graph_1_5_dir,'outInMatrix.txt'))

print('Dãy bậc ra của đồ thị G_15:',end =" ")
for i in G_15.Nodes:
    if i != G_15.Nodes[-1]  : 
        print(G_15.deg_out(i),'->', end =" ")
    else:
        print(G_15.deg_out(i))

print('Dãy bậc vào của đồ thị G_15:',end =" ")
for i in G_15.Nodes:
    if i != G_15.Nodes[-1]  : 
        print(G_15.deg_in(i),'->', end =" ")
    else:
        print(G_15.deg_in(i))
G_15.SCC()
#Display  Graphs
G_15.display_node()
G_15.display_arc()
G_15.display_adjMatrix()
G_15.display_inInMatrix()
G_15.display_outInMatrix()