from collections import deque
import sys

def bfs(k,v):
    queue = deque()
    visited = [False] * (N+1)
    visited[v] = True
    count = 0
    for ki,vi in network[v]:
        if ki >= k:
            queue.append(vi)
            visited[vi] = True
            count += 1
    while queue:
        q  = queue.popleft()
        for ki,vi in network[q]:
            if visited[vi] == False and ki >= k:
                queue.append(vi)
                visited[vi] = True
                count += 1
    print(count)
    
N,Q = map(int,sys.stdin.readline().split())
network = [[]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    p,q,r = map(int,sys.stdin.readline().split())
    network[p].append((r,q))
    network[q].append((r,p))
    
for _ in range(Q):
    k,v =  map(int, sys.stdin.readline().split())
    bfs(k,v)