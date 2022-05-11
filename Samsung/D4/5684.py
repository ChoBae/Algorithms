# 운동
from collections import deque
def dfs(b, start):
    visited = [0] * len(b)
    need_visited = deque()
    total = 0
    need_visited.append(start)
    while need_visited:
        
        target = need_visited.popleft()
        if not visited[target]:
            visited[target] += 1
            for now in b[target]:
                need_visited.append(now[0])
                total += now[1]
                
        return total    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    b = [[] for _ in range(n+1)]
    answer = 999999
    for _ in range(m):
        s, e, c = map(int, input().split())
        b[s].append((e,c))
    
    for i in range(len(b)-1):
        answer = min(answer, dfs(b, i+1))
    
    print(f"#{test_case} {answer}")
