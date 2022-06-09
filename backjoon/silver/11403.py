# 경로 찾기 실버1
# dfs 활용 -> 해당 i일때 갈 수 있는 방문체크
def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
# 입력
n = int(input())
graph = [[] for _ in range(n+1)]
# 그래프 입력 단계 -> 경로 선상으로 보기편하게 입력
for i in range(1,n+1):
    tmps = list(map(int, input().split()))
    for j in range(len(tmps)):
        if tmps[j] == 1:
            graph[i].append(j+1)
# i마다 dfs로 방문 체크
for i in range(1,n+1):
    visited = [False] * (n+1)
    dfs(i)
    # 해당 지점 갈 수 있는지 체크 후 출력
    for j in range(1,n+1):
        if visited[j]:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
