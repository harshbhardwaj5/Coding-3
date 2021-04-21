class graph:
    def __init__(self,Nodes,isdirected=False):
        self.nodes=Nodes          #Nodes bhejj d ilike a,b,c,d
        self.adjlist={}
        # self.isdirected=isdirected

        for i in self.nodes:
            self.adjlist[i]=[]              #empty adjlist A:[],B:[]

    def Edgeadd(self,source,des):
        self.adjlist[source].append(des)
        # if self.isdirected==True:
        #     self.adjlist[des].append(source)
    
    def printgraph(self):
        
        for i in self.nodes:
            print(i, '-> ',self.adjlist[i])


    
        
    def BFS(self):
        from queue import Queue
        visited={}
        ls=[]
        for i in self.adjlist.keys():
            visited[i]=False 
        queue=Queue()
        s=self.nodes[0]
        queue.put(s)
        visited[s]=True
        while not queue.empty():
            u=queue.get() 
            ls.append(u)

            for v in self.adjlist[u]:
                if not visited[v]:
                    visited[v]=True 
                    queue.put(v)
        print("The BFS traversal is->" ,ls)
       

    def DFS(self,node,visited):
        if node not in visited:
             visited.append(node)
             for v in self.adjlist[node]:
                g.DFS(v,visited)                 #important call it via g.dfs() not only dfs()
        
        return visited




g=graph(["A","B","C","D","E","F"],False)
edges=[('A','B'),('B','D'),('A','C'),('C','E'),('C','F')]
for u,v in edges:
    g.Edgeadd(u,v)
g.printgraph()
g.BFS()
print("The DFS traversal is -> ",g.DFS("A",[]))