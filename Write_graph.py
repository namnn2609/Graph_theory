import os
import copy
import numpy as np
from Graph_tool import multigraph as mg;
from Graph_tool import direct_multigraph as dmg;

# Wecome !
# This file we read and write some component of graph: node, arc, adjMatrix, Incidence matrix.
Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph' # This direction which you must be config.

#Create some folders
Graph_1_1_dir=os.path.join(Graph_dir,'Graph_1_1')
Graph_1_5_dir=os.path.join(Graph_dir,'Graph_1_5')
Graph_1_12_dir=os.path.join(Graph_dir,'Graph_1_12')
Graph_1_13_dir=os.path.join(Graph_dir,'Graph_1_13')
Graph_1_18_dir=os.path.join(Graph_dir,'Graph_1_18')
Graph_1_29_dir=os.path.join(Graph_dir,'Graph_1_29')
Graph_3_3_dir = os.path.join(Graph_dir,'Graph_3_3')

if not os.path.isdir(Graph_1_1_dir):
    os.makedirs(os.path.join(Graph_1_1_dir))

if not os.path.isdir(Graph_1_5_dir):
    os.makedirs(os.path.join(Graph_1_5_dir))

if not os.path.isdir(Graph_1_12_dir):
    os.makedirs(os.path.join(Graph_1_12_dir))

if not os.path.isdir(Graph_1_13_dir):
    os.makedirs(os.path.join(Graph_1_13_dir))

if not os.path.isdir(Graph_1_18_dir):
    os.makedirs(os.path.join(Graph_1_18_dir))

if not os.path.isdir(Graph_1_29_dir):
    os.makedirs(os.path.join(Graph_1_29_dir))

if not os.path.isdir(Graph_3_3_dir):
    os.makedirs(os.path.join(Graph_3_3_dir))
#We write Graph to file. First, Graph 1.1 (page 2).
G=dmg(5,10)
G.set_node(["1","2","3","4","5"])
G.set_arc(["(1,2)","(2,2)","(2,3)","(2,5)","(3,5)","(4,4)","(4,1)","(4,5)","(5,3)","(5,4)"]);

#Write node and arc to file.
G.write_nodes(os.path.join(Graph_1_1_dir,'nodes.txt'))
G.write_arcs(os.path.join(Graph_1_1_dir,'arcs.txt'))

#Generate adjMatrix and Incidence matrix.
G.generate_adjMatrix()
G.generate_in_out_InMatrix()

# Write to file.
G.write_inInMatrix(os.path.join(Graph_1_1_dir,'inInMatrix.txt'))
G.write_outInMatrix(os.path.join(Graph_1_1_dir,'outInMatrix.txt'))

#similarly for Graph Graph 1.12 (page 11 )
G_12=dmg(6,8)
G_12.set_node(["1","2","3","4","5","6"])
G_12.set_arc(["(1,2)","(2,3)","(2,4)","(3,1)","(4,2)","(4,5)","(5,6)","(6,4)"]);
G_12.generate_adjMatrix()
G_12.generate_in_out_InMatrix()
G_12.write_arcs(os.path.join(Graph_1_12_dir,'arcs.txt'))
G_12.write_nodes(os.path.join(Graph_1_12_dir,'nodes.txt'))
G_12.write_adjMatrix(os.path.join(Graph_1_12_dir,'adjMatrix.txt'))
G_12.write_inInMatrix(os.path.join(Graph_1_12_dir,'inInMatrix.txt'))
G_12.write_outInMatrix(os.path.join(Graph_1_12_dir,'outInMatrix.txt'))
G_12.Weight= [ [0, 1,  0,  0,  0,  0],
    [0, 0,  1,  1,  0,  0],
    [1, 0,  0,  0,  0,  0],
    [0, 1,  0,  0,  1,  0],
    [0, 0,  0,  0,  0,  1],
    [0, 0,  0,  1,  0,  0]]
G_12.write_Weight(os.path.join(Graph_1_12_dir,'WeightMatrix.txt'))   

G_13=dmg(9,19)
G_13.set_node(["1","2","3","4","5","6","7","8","9"])
G_13.set_arc(["(1,1)","(1,2)","(1,3)","(2,1)","(2,5)","(3,4)","(4,4)","(4,2)","(4,5)","(5,6)","(5,8)","(6,6)","(6,7)","(6,8)","(7,6)","(7,9)","(8,9)","(9,8)","(9,9)"]);
G_13.generate_adjMatrix()
G_13.generate_in_out_InMatrix()
G_13.write_arcs(os.path.join(Graph_1_13_dir,'arcs.txt'))
G_13.write_nodes(os.path.join(Graph_1_13_dir,'nodes.txt'))
G_13.write_adjMatrix(os.path.join(Graph_1_13_dir,'adjMatrix.txt'))
G_13.write_inInMatrix(os.path.join(Graph_1_13_dir,'inInMatrix.txt'))
G_13.write_outInMatrix(os.path.join(Graph_1_13_dir,'outInMatrix.txt'))

G_18=dmg(6,9)
G_18.set_node(["0","1","2","3","4","5"])
G_18.set_arc(["(0,2)","(0,4)","(1,0)","(2,3)","(2,4)","(3,2)","(3,5)","(4,5)","(5,4)"]);
G_18.generate_adjMatrix()
G_18.generate_in_out_InMatrix()
G_18.write_arcs(os.path.join(Graph_1_18_dir,'arcs.txt'))
G_18.write_nodes(os.path.join(Graph_1_18_dir,'nodes.txt'))
G_18.write_adjMatrix(os.path.join(Graph_1_18_dir,'adjMatrix.txt'))
G_18.write_inInMatrix(os.path.join(Graph_1_18_dir,'inInMatrix.txt'))
G_18.write_outInMatrix(os.path.join(Graph_1_18_dir,'outInMatrix.txt'))
G_18.Weight=[
    [0, 0,  1,  0,  5,  0],
    [3, 0,  0,  0,  0,  0],
    [0, 0,  0,  2,  2,  0],
    [0, 0,  3,  0,  0,  1],
    [0, 0,  0,  0,  0,  2],
    [0, 0,  0,  0,  1,  0]]
G_18.write_Weight(os.path.join(Graph_1_18_dir,'WeightMatrix.txt'))

G_29=dmg(6,6)
G_29.set_node(["1","2","3","4","5","6"])
G_29.set_arc(["(1,3)","(2,3)","(3,4)","(4,5)","(5,6)","(6,4)"]);
G_29.generate_adjMatrix()
G_29.generate_in_out_InMatrix()

G_29.write_arcs(os.path.join(Graph_1_29_dir,'arcs.txt'))
G_29.write_nodes(os.path.join(Graph_1_29_dir,'nodes.txt'))
G_29.write_adjMatrix(os.path.join(Graph_1_29_dir,'adjMatrix.txt'))
G_29.write_inInMatrix(os.path.join(Graph_1_29_dir,'inInMatrix.txt'))
G_29.write_outInMatrix(os.path.join(Graph_1_29_dir,'outInMatrix.txt'))

G_33=mg(12,11)
G_33.Vertices=['1', '2', '3', '4', '5','6','7','8','9','10','11','12']
G_33.Edges=['(1,2)',
             '(1,3)',
             '(2,4)',
             '(2,5)',
             '(4,8)',
             '(4,9)',
             '(3,7)',
           '(3,6)',
           '(6,10)',
           '(6,11)',
           '(7,12)']

G_33.generate_adjMatrix()
G_33.generate_InMatrix()
G_33.write_edges(os.path.join(Graph_3_3_dir,'edges.txt'))
G_33.write_vertex(os.path.join(Graph_3_3_dir,'vertex.txt'))
G_33.write_adjMatrix(os.path.join(Graph_3_3_dir,'adjMatrix.txt'))
G_33.write_InMatrix(os.path.join(Graph_3_3_dir,'InMatrix.txt'))


G_15=dmg(4,8)
G_15.set_node(["1","2","3","4"])
G_15.set_arc(["(1,2)","(2,4)","(2,4)","(1,4)","(4,1)","(4,3)","(3,1)","(3,1)"]);
G_15.generate_adjMatrix()
G_15.generate_in_out_InMatrix()
G_15.generate_adjMatrix()
G_15.generate_in_out_InMatrix()
G_15.write_arcs(os.path.join(Graph_1_5_dir,'arcs.txt'))
G_15.write_nodes(os.path.join(Graph_1_5_dir,'nodes.txt'))
G_15.write_adjMatrix(os.path.join(Graph_1_5_dir,'adjMatrix.txt'))
G_15.write_inInMatrix(os.path.join(Graph_1_5_dir,'inInMatrix.txt'))
G_15.write_outInMatrix(os.path.join(Graph_1_5_dir,'outInMatrix.txt'))