#!/usr/bin/env python
# coding: utf-8

# In[82]:


from Graph_tool import multigraph as mg;
from Graph_tool import direct_multigraph as dmg;
import numpy as np
import sys
import os
import copy


# In[2]:


Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'
os.listdir(Graph_dir)


# In[3]:


Graph_1_1_dir=os.path.join(Graph_dir,'Graph_1_1')
os.listdir(Graph_1_1_dir)


# # Graph 1.1 (trang 2)

# In[3]:


G=dmg(5,10)
G.set_node(["1","2","3","4","5"])
G.set_arc(["(1,2)","(2,2)","(2,3)","(2,5)","(3,5)","(4,4)","(4,1)","(4,5)","(5,3)","(5,4)"]);


# In[35]:


G.write_nodes(os.path.join(Graph_1_1_dir,'nodes.txt'))
G.write_arcs(os.path.join(Graph_1_1_dir,'arcs.txt'))


# In[4]:


G.generate_adjMatrix()
G.generate_in_out_InMatrix()


# In[5]:


G.inInMatrix


# In[6]:


G.outInMatrix


# In[7]:


G.adjMatrix


# In[32]:


G.write_inInMatrix(os.path.join(Graph_1_1_dir,'inInMatrix.txt'))
G.write_outInMatrix(os.path.join(Graph_1_1_dir,'outInMatrix.txt'))


# # Graph 1.12 (trang 11 sách tiếng việt)

# In[12]:


Graph_1_12_dir=os.path.join(Graph_dir,'Graph_1_12')
if not os.path.isdir(Graph_1_12_dir):
    os.makedirs(os.path.join(Graph_1_12_dir))


# In[16]:


G_12=dmg(6,8)
G_12.set_node(["1","2","3","4","5","6"])
G_12.set_arc(["(1,2)","(2,3)","(2,4)","(3,1)","(4,2)","(4,5)","(5,6)","(6,4)"]);


# In[20]:


G_12.generate_adjMatrix()
G_12.generate_in_out_InMatrix()


# In[22]:


G_12.adjMatrix


# In[24]:


G_12.inInMatrix


# In[25]:


G_12.outInMatrix


# In[29]:


G_12.TRANSITIVECLOSURESUCC('4')


# In[30]:


G_12.write_arcs(os.path.join(Graph_1_12_dir,'arcs.txt'))
G_12.write_nodes(os.path.join(Graph_1_12_dir,'nodes.txt'))
G_12.write_adjMatrix(os.path.join(Graph_1_12_dir,'adjMatrix.txt'))
G_12.write_inInMatrix(os.path.join(Graph_1_12_dir,'inInMatrix.txt'))
G_12.write_outInMatrix(os.path.join(Graph_1_12_dir,'outInMatrix.txt'))


# # Graph 1.13 (trang 12 sách tiếng việt)

# In[4]:


Graph_1_13_dir=os.path.join(Graph_dir,'Graph_1_13')
if not os.path.isdir(Graph_1_13_dir):
    os.makedirs(os.path.join(Graph_1_13_dir))


# In[5]:


G_13=dmg(9,19)
G_13.set_node(["1","2","3","4","5","6","7","8","9"])
G_13.set_arc(["(1,1)","(1,2)","(1,3)","(2,1)","(2,5)","(3,4)","(4,4)","(4,2)","(4,5)","(5,6)","(5,8)","(6,6)","(6,7)","(6,8)","(7,6)","(7,9)","(8,9)","(9,8)","(9,9)"]);


# In[6]:


G_13.generate_adjMatrix()


# In[7]:


G_13.adjMatrix


# In[8]:


G_13.generate_in_out_InMatrix()


# In[9]:


G_13.outInMatrix


# In[10]:


G_13.inInMatrix


# In[12]:


G_13.write_arcs(os.path.join(Graph_1_13_dir,'arcs.txt'))
G_13.write_nodes(os.path.join(Graph_1_13_dir,'nodes.txt'))
G_13.write_adjMatrix(os.path.join(Graph_1_13_dir,'adjMatrix.txt'))
G_13.write_inInMatrix(os.path.join(Graph_1_13_dir,'inInMatrix.txt'))
G_13.write_outInMatrix(os.path.join(Graph_1_13_dir,'outInMatrix.txt'))


# In[11]:


G_13.TRANSITIVECLOSURESUCC('5')


# # Graph 1.18 trang 21 sách tiếng việt

# In[31]:


Graph_1_18_dir=os.path.join(Graph_dir,'Graph_1_18')
if not os.path.isdir(Graph_1_18_dir):
    os.makedirs(os.path.join(Graph_1_18_dir))


# In[32]:


G_18=dmg(6,9)
G_18.set_node(["0","1","2","3","4","5"])
G_18.set_arc(["(0,2)","(0,4)","(1,0)","(2,3)","(2,4)","(3,2)","(3,5)","(4,5)","(5,4)"]);


# In[35]:


G_18.generate_adjMatrix()
G_18.generate_in_out_InMatrix()


# In[36]:


G_18.adjMatrix


# In[38]:


G_18.inInMatrix


# In[39]:


G_18.outInMatrix


# In[37]:


G_18.Weight=[
    [0, 0,  1,  0,  5,  0],
    [3, 0,  0,  0,  0,  0],
    [0, 0,  0,  2,  2,  0],
    [0, 0,  3,  0,  0,  1],
    [0, 0,  0,  0,  0,  2],
    [0, 0,  0,  0,  1,  0]]
G_18.write_Weight(os.path.join(Graph_1_18_dir,'WeightMatrix.txt'))
G_18.Weight


# In[47]:


G_18.write_arcs(os.path.join(Graph_1_18_dir,'arcs.txt'))
G_18.write_nodes(os.path.join(Graph_1_18_dir,'nodes.txt'))
G_18.write_adjMatrix(os.path.join(Graph_1_18_dir,'adjMatrix.txt'))
G_18.write_inInMatrix(os.path.join(Graph_1_18_dir,'inInMatrix.txt'))
G_18.write_outInMatrix(os.path.join(Graph_1_18_dir,'outInMatrix.txt'))


# # Graph 1.29 trang 41 sách tiếng anh (rig16)

# In[45]:


Graph_1_29_dir=os.path.join(Graph_dir,'Graph_1_29')
if not os.path.isdir(Graph_1_29_dir):
    os.makedirs(os.path.join(Graph_1_29_dir))


# In[46]:


G_29=dmg(6,6)
G_29.set_node(["1","2","3","4","5","6"])
G_29.set_arc(["(1,3)","(2,3)","(3,4)","(4,5)","(5,6)","(6,4)"]);


# In[86]:


G_29.generate_adjMatrix()
G_29.generate_in_out_InMatrix()


# In[50]:


G_29.write_arcs(os.path.join(Graph_1_29_dir,'arcs.txt'))
G_29.write_nodes(os.path.join(Graph_1_29_dir,'nodes.txt'))
G_29.write_adjMatrix(os.path.join(Graph_1_29_dir,'adjMatrix.txt'))
G_29.write_inInMatrix(os.path.join(Graph_1_29_dir,'inInMatrix.txt'))
G_29.write_outInMatrix(os.path.join(Graph_1_29_dir,'outInMatrix.txt'))


# In[93]:


def ROYWARSHALL(adjMatrix):
    m=copy.deepcopy(adjMatrix)
    for i in range(len(m)):
        m[i,i]=1
    print(m)
    for k in range(len(m)):
        for i in range(len(m)):
            for j in range(len(m)):
                m[i][j] = m[i][j] or( m[i][k] and m[k][j]);  
    return m


# In[92]:


G_29.adjMatrix


# In[94]:


ROYWARSHALL(G_29.adjMatrix)


# In[42]:


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

    for cout in range(len(graph)): 

        u = min_distance(dist, sptSet) 
        
        sptSet[u] = True
        
        for v in range(len(graph)): 
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
    printSolution(dist,len(graph))


# In[43]:


dijkstra(G_18.Weight,0)


# In[44]:


dijkstra(G_18.Weight,1)


# In[100]:


G_13.Arcs


# In[104]:


def succ(u):
    k=0
    result=[]
    for i in G_13.outInMatrix[int(u)-1]:
        if i==1:
            comma=int(G_13.Arcs[k].find(','))
            result.append(G_13.Arcs[k][comma+1:-1])
        k+=1
    return result


# In[105]:


def SPANNINGTREE(G_13):
    Component=[]
    New=[]
    Edges=[]
    Component.append(G_13.Nodes[0])
    New.append(G_13.Nodes[0])
    while len(New)!=0:
        Neighbors=[]
        for n in New:
            Neighbors=list(set(Neighbors+succ(n)))
            New=list(set(Neighbors) - set(Component))
        for v in New:
            for i in range(len(G_13.Arcs)):
                comma=int(G_13.Arcs[i].find(','))
                a=G_13.Arcs[1:comma]
                b=G_13.Arcs[comma+1:-1]
                if b in Component:
                    Edges.append(G_13.Arcs[i])
                    Component=list(set(Component+New))
    if Component != G_13.Arcs:
        return('Error: G is not connected')
    else:
        return(Component,Edges)
                


# In[ ]:


SPANNINGTREE(G_13)


# In[ ]:




