# 바이러스 실버3
import sys
from collections import deque
input = sys.stdin.readline

# 입력
t = int(input())
n = int(input())
# 그래프 , 방문여부 리스트 생성
graph = [[] for _ in range(t+1)]
visited = [False] * (t+1)
# 노드 입력받기
for _ in range(n):
    start, end  = map(int, input().split())
    graph[start].append(end)
    graph[end].append(end)
# 1번 컴퓨터부터 시작
queue = deque([1])
visited[1] = True
answer = 0
# bfs
while queue:
    state = queue.popleft()
    answer += 1
    for i in graph[state]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            
print(answer-1)



