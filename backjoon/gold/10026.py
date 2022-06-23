from collections import deque
# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# bfs 진행 -> 적록 탐색을 여기에 넣어주면 후에 재사용이 불편할거라고 생각해서 넣기 싫었다..
def bfs(x, y, ver):
    q = deque([(x, y)])
    visited[x][y] = True    # 현재 좌표 방문처리
    stateCol = grid[x][y]   # 현재 좌표의 색상
    # 적록 색약시 빨강과 그린을 넣어줌
    if ver == 1 and (stateCol == 'G' or stateCol == 'R'):
        stateCol = ['R', 'G']
    # bfs 진행
    while q:
        px, py = q.popleft()
        # 상하좌우 진행
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            # 좌표가 그리드의 틀을 벗어나지 않을때
            if 0 <= nx <= len(grid)-1 and 0 <= ny <= len(grid)-1:
                # 탐색 여부와 현재 색과 같을때 큐에 넣어준다
                if not visited[nx][ny] and grid[nx][ny] in stateCol:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return


# 적록색약
n = int(input())    # n x n의 그리드
grid = []
answer = [0] * 2    # 정답
# 1.그리드 생성
for _ in range(n):
    grid.append(list(input()))

# 2. 두가지 경우 따로 구하기
for step in range(2):
    visited = [[False] * n for _ in range(n)]   # 방문 여부 초기화
    cnt = 0  # 구역 수 초기화
    # 적록색약이 아닐경우
    if step == 0:
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    bfs(i, j, step)
                    cnt += 1
        answer[0] = cnt
    # 적록색약일 경우
    else:
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    bfs(i, j, step)
                    cnt += 1
        answer[1] = cnt
# 출력
print(*answer)
