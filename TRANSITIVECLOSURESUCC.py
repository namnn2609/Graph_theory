import sys
import os
import copy
import numpy as np
from Graph_tool import multigraph as mg;
from Graph_tool import direct_multigraph as dmg;


Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'
Graph_1_12_dir=os.path.join(Graph_dir,'Graph_1_12')
Graph_1_13_dir=os.path.join(Graph_dir,'Graph_1_13')

G_12=dmg(6,8)
G_12.read_nodes(os.path.join(Graph_1_12_dir,'nodes.txt'))
G_12.read_arcs(os.path.join(Graph_1_12_dir,'arcs.txt'))
G_12.read_adjMatrix(os.path.join(Graph_1_12_dir,'adjMatrix.txt'))
G_12.read_inInMatrix(os.path.join(Graph_1_12_dir,'inInMatrix.txt'))
G_12.read_outInMatrix(os.path.join(Graph_1_12_dir,'outInMatrix.txt'))

G_13=dmg(9,19)
G_13.read_nodes(os.path.join(Graph_1_13_dir,'nodes.txt'))
G_13.read_arcs(os.path.join(Graph_1_13_dir,'arcs.txt'))
G_13.read_adjMatrix(os.path.join(Graph_1_13_dir,'adjMatrix.txt'))
G_13.read_inInMatrix(os.path.join(Graph_1_13_dir,'inInMatrix.txt'))
G_13.read_outInMatrix(os.path.join(Graph_1_13_dir,'outInMatrix.txt'))

result=G_12.TRANSITIVECLOSURESUCC('1')
print(' result of G_12 with vertex 1: ',result)
result=G_13.TRANSITIVECLOSURESUCC('9')
print(' result of G_13 with vertex 9 ',result)