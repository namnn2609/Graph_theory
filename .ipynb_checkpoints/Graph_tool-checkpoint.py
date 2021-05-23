import sys
import numpy as np 
class multigraph:
    def __init__(self,nbver,nbedge):
        self.Nver = nbver
        self.Nedge = nbedge
        self.Vertices = []
        self.Edges = []
        self.adjMatrix = np.zeros((self.Nver,self.Nver),dtype=np.uint) 
        self.inMatrix = np.zeros((self.Nver,self.Nedge),dtype=np.uint)
    def set_vertex(self,vert_list):
        for vertex in vert_list:
            self.Vertices.append(vertex);
        return self;
    def set_edge(self,Edges_list):
        for edge in Edges_list:
            self.Edges.append(edge);
        return self;
    def set_adjMatrix(self,i,j,x):
        nrow = self.adjMatrix.shape[0];
        ncol = self.adjMatrix.shape[1];
        if ((i>=nrow)or(j>=ncol)):
            print("Out of range!");
        else:
            self.adjMatrix[i,j] = x;
        return self;
    def set_inMatrix(self,i,j,x):
        nrow = self.inMatrix.shape[0];
        ncol = self.inMatrix.shape[1];
        if ((i>=nrow)or(j>=ncol)):
            print("Out of range!");
        else:
            self.inMatrix[i,j] = x;
        return self;
    
    def display_vertex(self):
        VERTS = self.Vertices;
        print("List of vertex(ices)")
        for k in range(0,len(VERTS)):
            print(VERTS[k]);
    def display_edge(self):
        EDGES = self.Edges;
        print("List of edge(s)")
        for k in range(0,len(EDGES)):
            print(EDGES[k]); 
    def display_adjMatrix(G):
        print("Adjacency matrix");
        M = G.adjMatrix;
        print(M);
    def display_inMatrix(G):
        print("Incidence matrix");
        M = G.inMatrix;
        print(M);

##Here is your workspace. Adding your own code to use in chosen practical work
##on unoriented multigraph.
    def generate_adjMatrix(self):
        for Edge in self.Edges:
            comma=int(Edge.find(','))
            a=Edge[1:comma]
            b=Edge[comma+1:-1]
            print(a,b)
            self.adjMatrix[self.Vertices.index(a),self.Vertices.index(b)] =1
            self.adjMatrix[self.Vertices.index(b),self.Vertices.index(a)] =1
    
    def generate_InMatrix(self):
        for i in range(len(self.Edges)):
            comma=int(self.Edges[i].find(','))
            a=self.Edges[i][1:comma]
            b=self.Edges[i][comma+1:-1]
            self.inMatrix[self.Vertices.index(a),i] =1
            self.inMatrix[self.Vertices.index(b),i] =1

    def write_vertex(self,the_filename):
        with open(the_filename, 'w') as file:
            for v in self.Vertices:
                file.write('%s\n' % v)
            file.close()
            
    def read_vertex(self,the_filename):
        with open(the_filename, 'r') as filehandle:
            filecontents = filehandle.readlines()

            for line in filecontents:
                current_place = line[:-1]
                self.Vertices.append(current_place)
            filehandle.close()

            
    def write_edges(self,the_filename):
        with open(the_filename, 'w') as file:
            for v in self.Edges:
                file.write('%s\n' % v)
            file.close()
            
    def read_edges(self,the_filename):
        with open(the_filename, 'r') as filehandle:
            filecontents = filehandle.readlines()
            for line in filecontents:
                current_place = line[:-1]
                self.Edges.append(current_place)
            filehandle.close()
            
    def write_adjMatrix(self,filename):
        np.savetxt(filename, self.adjMatrix, fmt= '%5.0f')
        
    def read_adjMatrix(self,filename):
        y = np.loadtxt(filename)
        self.adjMatrix=y.astype(int)
        
        
    def write_adjMatrix(self,filename):
        np.savetxt(filename, self.inMatrix, fmt= '%5.0f')
        
    def read_adjMatrix(self,filename):
        y = np.loadtxt(filename)
        self.inMatrix=y.astype(int)

    
##Good luck!
class direct_multigraph:
    def __init__(self,nbnode,nbarc):
        self.Nnode = nbnode;
        self.Narc = nbarc;
        self.Nodes = [];
        self.Arcs = [];
        self.adjMatrix = np.zeros((self.Nnode,self.Nnode),dtype=np.uint);
        self.inInMatrix = np.zeros((self.Nnode,self.Narc),dtype=np.uint);
        self.outInMatrix = np.zeros((self.Nnode,self.Narc),dtype=np.uint);
        self.Weight=np.zeros((self.Nnode,self.Nnode),dtype=np.uint);
    def set_node(self,node_list):
        for NODE in node_list:
            self.Nodes.append(NODE);
        return self;
    def set_arc(self,arc_list):
        for ARC in arc_list:
            self.Arcs.append(ARC);
        return self;
    def set_adjMatrix(self,i,j,x):
        nr = self.adjMatrix.shape[0];
        nc = self.adjMatrix.shape[1];
        if (i>=nr or j>= nc):
            print("Out of range!");
        else:
            self.adjMatrix[i,j] = x;
        return self;
    def set_inInMatrix(self,i,j,x):
        nr = self.inInMatrix.shape[0];
        nc = self.inInMatrix.shape[1];
        if (i>=nr or j>= nc):
            print("Out of range!");
        else:
            self.inInMatrix[i,j] = x;
        return self;
    def set_outInMatrix(self,i,j,x):
        nr = self.outInMatrix.shape[0];
        nc = self.outInMatrix.shape[1];
        if (i>=nr or j>= nc):
            print("Out of range!");
        else:
            self.outInMatrix[i,j] = x;
        return self;
    
    def display_node(self):
        print("List of node(s)");
        NODES = self.Nodes;
        for k in range(0,len(NODES)):
            print(NODES[k]);
    def display_arc(self):
        print("List of arc(s)");
        ARCS = self.Arcs;
        for k in range(0,len(ARCS)):
            print(ARCS[k]);
    def display_adjMatrix(self):
        print("Adjacency matrix");
        M = self.adjMatrix;
        print(M);
    def display_inInMatrix(self):
        print("Incoming incidence matrix");
        M = self.inInMatrix;
        print(M);
    def display_outInMatrix(self):
        print("Outgoing incidence matrix");
        M = self.outInMatrix;
        print(M);
    def display_Weight(self):
        print("Adjacency matrix");
        M = self.Weight;
        print(M);
##Here is your workspace. Adding your own code to use in chosen practical work
##on directed multigraph.
##Good luck!
    def generate_adjMatrix(self):
        for Arc in self.Arcs:
            comma=int(Arc.find(','))
            a=int(Arc[1:comma])
            b=int(Arc[comma+1:-1])
            self.adjMatrix[a-1,b-1] +=1
    
    def generate_in_out_InMatrix(self):
        for i in range(len(self.Arcs)):
            comma=int(self.Arcs[i].find(','))
            a=int(self.Arcs[i][1:comma])
            b=int(self.Arcs[i][comma+1:-1])
            self.inInMatrix[b-1,i] +=1
            self.outInMatrix[a-1,i] +=1
            
    def deg_in(self,v):
        index=self.Nodes.index(v)
        result= self.inInMatrix[self.Nodes.index(v)].sum()
        return result
    
    def deg_out(self,v):
        index=self.Nodes.index(v)
        result= np.abs(self.outInMatrix[self.Nodes.index(v)].sum())
        return result
            
    def write_nodes(self,the_filename):
        with open(the_filename, 'w') as file:
            for n in self.Nodes:
                file.write('%s\n' % n)
            file.close()
            
    def read_nodes(self,the_filename):
        with open(the_filename, 'r') as filehandle:
            filecontents = filehandle.readlines()
            for line in filecontents:
                current_place = line[:-1]
                self.Nodes.append(current_place)
            filehandle.close()
            
    def write_arcs(self,the_filename):
        with open(the_filename, 'w') as file:
            for v in self.Arcs:
                file.write('%s\n' % v)
            file.close()
            
    def read_arcs(self,the_filename):
        with open(the_filename, 'r') as filehandle:
            filecontents = filehandle.readlines()
            for line in filecontents:
                current_place = line[:-1]
                self.Arcs.append(current_place)
            filehandle.close()
            
            
    def write_adjMatrix(self,filename):
        np.savetxt(filename, self.adjMatrix, fmt= '%5.0f')
        
    def read_adjMatrix(self,filename):
        y = np.loadtxt(filename)
        self.adjMatrix=y.astype(int)
        
        
    def write_inInMatrix(self,filename):
        np.savetxt(filename, self.inInMatrix, fmt= '%5.0f')
        
    def read_inInMatrix(self,filename):
        y = np.loadtxt(filename)
        self.inInMatrix=y.astype(int)
        
        
    def write_outInMatrix(self,filename):
        np.savetxt(filename, self.outInMatrix, fmt= '%5.0f')
        
    def read_outInMatrix(self,filename):
        y = np.loadtxt(filename)
        self.outInMatrix=y.astype(int)
        
    def write_Weight(self,filename):
        np.savetxt(filename, self.Weight, fmt= '%5.0f')
        
    def read_Weight(self,filename):
        y = np.loadtxt(filename)
        self.Weight=y.astype(int)
    def succ(self,u):
        k=0
        result=[]
        for i in self.outInMatrix[int(u)-1]:
            if i==1:
                comma=int(self.Arcs[k].find(','))
                result.append(self.Arcs[k][comma+1:-1])
            k+=1
        return result
    def pred(self,u):
        k=0
        result=[]
        for i in self.inInMatrix[self.Nodes.index(u)]:
            if i==1:
                comma=int(self.Arcs[k].find(','))
                result.append(self.Arcs[k][1:comma])
            k+=1
        return result
    def TRANSITIVECLOSURESUCC(self,v):
        Component=[]
        New=[]
        Component.append(v)
        New.append(v)
        while len(New)!=0:
            Neighbors=[]
            for n in New:
                Neighbors=list(set(Neighbors+self.succ(n)))
            New=list(set(Neighbors) - set(Component))
            Component=list(set(Component+New))
        return Component
    def TRANSITIVECLOSUREPRED(self,v):
        Component=[]
        New=[]
        Component.append(v)
        New.append(v)
        while len(New)!=0:
            Neighbors=[]
            for n in New:
                Neighbors=list(set(Neighbors+self.pred(n)))
            New=list(set(Neighbors) - set(Component))
            Component=list(set(Component+New))
        return Component
    def SCC(self):
        results=[]
        for i in self.Nodes:
            suc = self.TRANSITIVECLOSURESUCC(i)
            pre = self.TRANSITIVECLOSUREPRED(i)
            con = list(set(suc).intersection(set(pre)))
            con.sort()
            if con not in results:
                results.append(con)
    
        print('SCC :',results)
        
        
