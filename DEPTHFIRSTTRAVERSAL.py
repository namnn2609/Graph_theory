import os 
from Graph_tool import multigraph as mg;
# G_33=mg(12,11)
# G_33.Vertices=['1', '2', '3', '4', '5','6','7','8','9','10','11','12']
# G_33.Edges=['(1,2)',
#              '(1,3)',
#              '(2,4)',
#              '(2,5)',
#              '(4,8)',
#              '(4,9)',
#              '(3,7)',
#            '(3,6)',
#            '(6,10)',
#            '(6,11)',
#            '(7,12)']
# G_33.generate_adjMatrix()
# G_33.generate_InMatrix()
G_33=mg(12,11)

Graph_dir=r'C:\Users\Mr Nam\Desktop\TP\Graph'
Graph_3_3_dir=os.path.join(Graph_dir,'Graph_3_3')

G_33.read_vertex(os.path.join(Graph_3_3_dir,'vertex.txt'))
G_33.read_edges(os.path.join(Graph_3_3_dir,'edges.txt'))
G_33.read_adjMatrix(os.path.join(Graph_3_3_dir,'adjMatrix.txt'))
G_33.read_InMatrix(os.path.join(Graph_3_3_dir,'InMatrix.txt'))

def DEPTHFIRSTTRAVERSAL(G,v1):
    def succ(G,u):
        s = []
        u = int(u)
        for i in range(len(G.Vertices)):
            if (G.adjMatrix[u-1,i]==1):
                s.append(G.Vertices[i])
        return s
    comp = list()
    comp.append(v1)
    while len(comp)!=len(G.Vertices):
        i = len(comp)
        X = list()
        s = succ(G,comp[i-1])
        for u in s:
            if u not in comp:
                X.append(u)
        while len(X)==0:
            i = i-1
            s1 = succ(G,comp[i-1])
            for u in s1:
                if u not in comp:
                    X.append(u)
        for u in X:
            comp.append(u)
            break
    print("dãy đỉnh tương ứng là: ")
    print(comp)
DEPTHFIRSTTRAVERSAL(G_33,'1')