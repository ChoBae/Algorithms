# 토마토 골드5 미완
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0 , 1, -1]
dl = [1, -1]
def bfs(x, y, l, box):
    global answer
    q = deque([(x, y, l)])
    visited[l][x][y] = True
    while q:
        px, py, pl = q.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            # if 0<= nx < x and 0<= ny <y:
    return
        
m, n, h = map(int, input().split())
box = [[] for _ in range(h)]
visited = [[] for _ in range(h)]

# 1 = 익은토마토 , 0 = 익지않은 토마토, -1 = 비어있는 칸
for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int, input().split())))
        visited[i].append([[False]*m])

answer = 0
for i in range(h):
    for j in range(n):
        for z in range(m):
            if box[i][j][z] == 1:
                bfs(i, j, z, box)
                