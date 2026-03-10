class Graph():
    def __init__(self,n):
        self.n = n
        self.adj = [[]*n for i in range(n)]

    def create_link(self,a,b):
        self.adj[a-1].append(b)
        self.adj[b-1].append(a)

    def show_result(self):
        for i in range(self.n):
            print(f"{i+1}: {self.adj[i]}")
    
    def check_neighbours(self,n_index):
        neighbours = len(self.adj[n_index])
        print(neighbours)
        return neighbours

    #Zoom 35
    def breadth_first_search(self, source):
        visited = [False]*self.n
        queue = []
        res = []

        queue.append(source)
        visited[source] = True
        while len(queue) > 0:
            a = queue[0]
            queue.pop(0)
            visited[a] = True
            res.append(a)
            for child in self.adj[a]:
                if visited[child] == False:
                    queue.append(child)
        return res

    #Zoom 36
    def DFSUtil(self,source,result,visited):
##        if visited==None:
##            visited=set()
        
        visited[source] = True
        result.append(source+1)

        for i in self.adj[source]:
            neighbour_index=i-1
            if visited[neighbour_index] == False:
                result = self.DFSUtil(neighbour_index,result,visited)
        return result

    def connected_components(self):
        visited = []
        cc = []

        for a in range(self.n):
            visited.append(False)
        for b in range(self.n):
            if visited[b] == False:
                temp = []
                cc.append(self.DFSUtil(b,temp,visited))
        return cc
    def check_fully_connected(self):
        visited = [False]*self.n
        self.DFSUtil(0,[],visited)
        for a in visited:
            if a == False:
                return False
        return True

        
            
        
def depth_first_search(graph,source,visited=None):
    if visited==None:
        visited=set() # sets can't have duplicate values

    visited.add(source)
    print(source, end="=")
    
    for neighbour in graph[source-1]:
        if neighbour not in visited:
            depth_first_search(graph,neighbour,visited)
    return visited

g1 = Graph(7)
g1.create_link(1,4)
g1.create_link(4,6)
g1.create_link(3,6)
g1.create_link(1,6)
g1.create_link(4,5)
g1.create_link(5,7)
g1.create_link(2,6)

g2 = Graph(5)
g2.create_link(2,1)
g2.create_link(2,3)
g2.create_link(3,5)
g2.create_link(1,4)
g2.show_result()
g2.check_neighbours(2)

#Zoom 35
print(g2.breadth_first_search(1)) # Give neighbours of 2: Note: 2-1=1
depth_first_search(g2.adj,2)
print("")

#Zoom 36

print(g2.connected_components())

print(g2.check_fully_connected())
