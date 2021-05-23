import sys
import os
import copy
import numpy as np
from Graph_tool import multigraph as mg;
from Graph_tool import direct_multigraph as dmg;

Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'

Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'
Graph_1_18_dir=os.path.join(Graph_dir,'Graph_1_18')

G_19=mg(6,7)

G_19.Vertices=['0', '1', '2', '3', '4', '5']
G_19.Edges=['(0,2)',
             '(0,4)',
             '(1,0)',
             '(2,3)',
             '(2,4)',
             '(3,5)',
             '(4,5)' ]
G_19.generate_InMatrix()
G_19.generate_adjMatrix()

def SPANNINGTREE(Graph):
    def succ(u):
        k=0
        result=[]
        for i in Graph.adjMatrix[Graph.Vertices.index(u)]:
            if i==1:
                result.append(Graph.Vertices[k])
            k+=1
        return result
    Component=[]
    New=[]
    Edges=[]
    Component.append(Graph.Vertices[0])
    New.append(Graph.Vertices[0])

    while len(New)!=0:

        Neighbors=[]
        for n in New:
            Neighbors=list(set(Neighbors+succ(n)))
            New=list(set(Neighbors) - set(Component))
        for v in New:
            for i in range(len(Graph.Edges)):
                comma=int(Graph.Edges[i].find(','))
                a=Graph.Edges[i][1:comma]
                b=Graph.Edges[i][comma+1:-1]
                if (a in Component):
                    if Graph.Edges[i] not in Edges:
                        Edges.append(Graph.Edges[i])
                    Component=list(set(Component+New))

    Component.sort()
    if Component != Graph.Vertices:
        return('Error: G is not connected')

    else:
        return(Component,Edges)
#print(SPANNINGTREE(G_19))
G_19.display_vertex()
G_19.display_edge()
G_19.display_adjMatrix()
G_19.display_inMatrix()
