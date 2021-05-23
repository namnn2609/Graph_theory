import sys
import os
import numpy as np
from Graph_tool import multigraph as mg;
from Graph_tool import direct_multigraph as dmg;

Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'
Graph_1_18_dir=os.path.join(Graph_dir,'Graph_1_18')
Graph_1_12_dir=os.path.join(Graph_dir,'Graph_1_12')

G_18=dmg(6,9)
G_18.read_nodes(os.path.join(Graph_1_18_dir,'nodes.txt'))
G_18.read_arcs(os.path.join(Graph_1_18_dir,'arcs.txt'))
G_18.read_adjMatrix(os.path.join(Graph_1_18_dir,'adjMatrix.txt'))
G_18.read_inInMatrix(os.path.join(Graph_1_18_dir,'inInMatrix.txt'))
G_18.read_outInMatrix(os.path.join(Graph_1_18_dir,'outInMatrix.txt'))
G_18.read_Weight(os.path.join(Graph_1_18_dir,'WeightMatrix.txt'))

G_12=dmg(6,8)
G_12.read_nodes(os.path.join(Graph_1_12_dir,'nodes.txt'))
G_12.read_arcs(os.path.join(Graph_1_12_dir,'arcs.txt'))
G_12.read_adjMatrix(os.path.join(Graph_1_12_dir,'adjMatrix.txt'))
G_12.read_inInMatrix(os.path.join(Graph_1_12_dir,'inInMatrix.txt'))
G_12.read_outInMatrix(os.path.join(Graph_1_12_dir,'outInMatrix.txt'))
G_12.read_Weight(os.path.join(Graph_1_12_dir,'WeightMatrix.txt'))

def min_distance(dist, sptSet):
    min_value = sys.maxsize 
    min_index=-1
    for v in range(len(dist)): 
        if dist[v] < min_value and sptSet[v] == False: 
            min_value = dist[v] 
            min_index = v 
    return min_index 

def printSolution( dist,number_value): 
    print("Vertex \tDistance from Source")
    for node in range(number_value): 
        print (node, "\t", dist[node])

def dijkstra(graph,src): 

    dist = [sys.maxsize] * len(graph)
    dist[src] = 0
    sptSet = [False] * len(graph)

    for _ in range(len(graph)): 

        u = min_distance(dist, sptSet) 
        
        sptSet[u] = True
        
        for v in range(len(graph)): 
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
    printSolution(dist,len(graph))

print('dijkstra with figure 1.21 start at v1(vertex 0)')
dijkstra(G_18.Weight,0)

print('dijkstra with figure 1.21 start at 1')
dijkstra(G_18.Weight,1)
print('dijkstra with figure 1.12 start at 1')
dijkstra(G_12.Weight,0)