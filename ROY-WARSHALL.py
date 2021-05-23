import os
import copy
import numpy as np
from Graph_tool import multigraph as mg;
from Graph_tool import direct_multigraph as dmg;

G_29=dmg(6,6)
Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'
Graph_1_29_dir=os.path.join(Graph_dir,'Graph_1_29')

G_29.read_nodes(os.path.join(Graph_1_29_dir,'nodes.txt'))
G_29.read_arcs(os.path.join(Graph_1_29_dir,'arcs.txt'))
G_29.read_adjMatrix(os.path.join(Graph_1_29_dir,'adjMatrix.txt'))
G_29.read_inInMatrix(os.path.join(Graph_1_29_dir,'inInMatrix.txt'))
G_29.read_outInMatrix(os.path.join(Graph_1_29_dir,'outInMatrix.txt'))

def ROYWARSHALL(adjMatrix):
    m=copy.deepcopy(adjMatrix)
    for i in range(len(m)):
        m[i,i]=1
    for k in range(len(m)):
        for i in range(len(m)):
            for j in range(len(m)):
                m[i][j] = m[i][j] or( m[i][k] and m[k][j]);  
    return m

print(ROYWARSHALL(G_29.adjMatrix))
