# DFS와 BFS
from collections import deque
# dfs
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
        

# bfs
def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    # 큐가 빌 때가지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소에 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                print(queue)
                visited[i] = True
                
# 그래프 값 리스트화
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [False for i in range(n+1)]

bfs_graph = graph
bfs_visited = visited
dfs_graph = graph
dfs_visited = visited

dfs(dfs_graph, v, dfs_visited)
print()
bfs(bfs_graph, v, bfs_visited)

