import os
import copy
import numpy as np
from Graph_tool import multigraph as mg;
from Graph_tool import direct_multigraph as dmg;


Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'
Graph_1_18_dir=os.path.join(Graph_dir,'Graph_1_18')
G_18=dmg(6,9)
G_18.read_nodes(os.path.join(Graph_1_18_dir,'nodes.txt'))
G_18.read_arcs(os.path.join(Graph_1_18_dir,'arcs.txt'))
G_18.read_adjMatrix(os.path.join(Graph_1_18_dir,'adjMatrix.txt'))
G_18.read_inInMatrix(os.path.join(Graph_1_18_dir,'inInMatrix.txt'))
G_18.read_outInMatrix(os.path.join(Graph_1_18_dir,'outInMatrix.txt'))

def TESTINGCYCLICITY(G):
        def source(node, inInMatrix):
            if len(node)==0: return "None"
            for i in node:
                d = 0
                for y in range(len(inInMatrix[0])):
                    d += inInMatrix[int(i) - 1,y]
                if d==0: 
                    return i
            return "None"
    
        inInMatrix = np.array(G.inInMatrix)
        while source(G.Nodes, inInMatrix)!="None":
            v = source(G.Nodes, inInMatrix)
            G.Nodes.remove(v)
            for i in range(len(G.Arcs)):
                comma=int(G.Arcs[i].find(','))
                a=int(G.Arcs[i][1:comma])
                b=int(G.Arcs[i][comma+1:-1])
                if a==int(v) or b==int(v):
                    for j in range(len(G.Nodes)):
                        inInMatrix[j,i] = 0
        if len(G.Nodes)==0:
            print("Graph has no cycle.")
        else:
            print("Graph has a cycle.")
print('test CYCLICITY of G_18:', end =" ")
TESTINGCYCLICITY(G_18)