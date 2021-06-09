import queue
# By using BFS algorith we find the minimum distance between node.
def min_distance(edges, u, v, node):
    distance_bw_node = [0] * node
    seen_node = [0] * node
    
    # Initially the distance is 0.
    distance_bw_node[u] = 0
    seen_node[u] = True
    Que = queue.Queue()
    Que.put(u)
    while (not Que.empty()):
        num = Que.get()
        for i in range(len(edges[num])):
            if (seen_node[edges[num][i]]):
                continue
            distance_bw_node[edges[num][i]] = distance_bw_node[num] + 1
            Que.put(edges[num][i])
            seen_node[edges[num][i]] = 1
    return distance_bw_node[v]
 

def addEdge(edges, u, v):
    edges[u].append(v)
    edges[v].append(u)

list_1 = list(map(int,input().split()))
n = list_1[0]
h = list_1[1]
x = list_1[2]
hotspot_list = list(map(int,input().split()))
edges = [[] for i in range(n)]
for i in range(n-1):
    l = list(map(int,input().split()))
    addEdge(edges,l[0]-1,l[1]-1)
        
epicente_list = hotspot_list
    
for i in range(n):
    if i+1 not in hotspot_list:
        status = 1
        for j in hotspot_list:
            dist = min_distance(edges, i, j-1, n)
            if dist > x:
                status = 0
                break
        if status == 1:
            epicente_list.append(i+1)
                
print (len(epicente_list))