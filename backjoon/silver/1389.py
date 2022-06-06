# 케빈 베이컨의 6단 법칙 실버1
from collections import deque
# bfs
def bfs(start):
    num = [0] * (n+1)
    q = deque([start])
    visited[start] = True
    while q:
        state = q.popleft()
        for i in graph[state]:
            if not visited[i]:
                num[i] = num[state] + 1
                q.append(i)
                visited[i] = True
    
    return sum(num)
    
n, m = map(int, input().split())    # n(사람수), m(친구관계 수)
# 친구관계 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b  = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 1번부터 n까지 검사
result = []
for i in range(1,n+1):
    visited = [False] * (n+1)
    result.append(bfs(i))
# 출력
print(result.index(min(result))+1)