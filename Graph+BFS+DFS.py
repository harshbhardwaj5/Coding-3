from collections import defaultdict

class graph:
    def __init__(self,Nodes,isdirected=False):
        self.nodes=Nodes          #Nodes bhejj d ilike a,b,c,d
        self.adjlist=defaultdict(list)
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




    def DFS(self,node,visited):
        if node not in visited:
            visited.append(node)
            for v in self.adjlist[node]:
                g.DFS(v,visited)
        return visited

    def DFSIterative(self):
        stack=[]
        visited={}
        visited={self.nodes[i]:False for i in range(len(self.nodes))}
        print(visited)

        stack.append(self.nodes[0])
        # visited[stack[-1]]=True
        while(len(stack)):
            s=stack[-1]
            
            stack.pop()
            if not visited[s]:
                print(s)
                visited[s]=True
            
            for i in self.adjlist[s]:
                    if visited[i]!=True:
                        stack.append(i)

    def isCyclicUtil(self, v, visited, recStack):
      
        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours
        # if any neighbour is visited and in 
        # recStack then graph is cyclic
        for neighbour in self.adjlist[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
  
        # The node needs to be poped from 
        # recursion stack before function ends
        recStack[v] = False
        return False                  
    def isCyclic(self):
        visited = [False] * 4
        recStack = [False] * 4
        for node in range(4):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False
    


g=graph([0,1,2,3],False)
# edges=[(0, 2),(1, 2),(2, 0),(2, 3),(3, 3)]
edges=[(0,2),(2,3),(1,4)]
for u,v in edges:
    g.Edgeadd(u,v)
g.printgraph()
g.BFS()
print("The DFS traversal is -> ",g.DFS(0,[]))
g.DFSIterative()
if g.isCyclic()==1:
    print("True")
else:
    print("False")
    (0, 1)
