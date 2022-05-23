# 최장 경로
# dfs
def dfs(v, start):
    global maxLen
    # 결과값 업데이트
    if maxLen < v:
        maxLen = v
        
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(v+1, i)
            visited[i] = False
            

# 입력
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())    # n(정점의 수), m(간선의 수)
    graph = [[] for _ in range(n+1)]    # 그래프
    maxLen = -10e9  # 결과값
    # 간선이 없을때
    if m == 0:
        maxLen = n
    else:
        # 그래프 생성
        for i in range(m):
            x, y = map(int, input().split())
            # 양방향 간선
            graph[x].append(y)
            graph[y].append(x)
        # 정점 마다 출발
        visited = [False] * (n+1)  # 방문여부 리스트
        for i in range(1, n+1):
            visited[i] = True  # 시작지점  초기화
            # dfs 시작
            dfs(1, i)
            visited[i] = False # 시작지점  초기화 
    # 출력
    print(f"#{tc} {maxLen}")
