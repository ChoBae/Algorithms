# 뱀과 사다리 게임 골드 5 
# 입력
from collections import deque


# n, m = map(int, input().split()) # n(사다리의 수), m(뱀의 수)
# lad, sna = [], []
# # 사다리 입력
# for _ in range(n):
#     x, y = map(int, input().split())
#     lad.append((x, y))
# # 뱀 입력
# for _ in range(m):
#     u, v = map(int, input().split())
#     # sna.append((u, v))
#     sna.append(u)
# lad.sort()
# sna.sort()

# # # 1. 게임 진행
# state, answer = 1, 0 # state(현재 위치(1부터 시작)), answer(주사위 굴린 갯수, 정답)
# while state <= 100:
#     # 사다리가 있을때 가장 큰 이동범위로 이동
#     tmp, next_state, move_check = 0, 0, True
#     for i in range(len(lad)):
#         x, y = lad[i][0], lad[i][1]
#         if x > state:
#             value = y - x
#             if state+6 < y and tmp < value:
#                 tmp = value
#                 next_state = y
#                 next_answer = x - state
#                 move_check = False

#     # 사다리가 없다면 무조건 6칸 이동하는게 가장 빠름
#     if move_check:
#         # 뱀 피해서 가기
#         for i in range(state, state+7):
#             if i not in sna:
#                 state = i
#         answer += 1 # 주사위 굴리기
#     # 사다리 이용
#     else:
#         state = next_state
#         answer += (next_answer//6) + 1   
        
# print(answer)

## 테케 답은나옴..
# bfs 풀이
def bfs(v):
    q = deque([v])
    # 큐가 빌때까지
    while q:
        target = q.popleft()
        # 주사위 눈만큼 탐색
        for i in range(1, 7):
            ran = target + i
            # 100칸 이상일때 무시
            if ran > 100:
                continue
            # 현재 위치에서 이동할 수 있는 좌표
            cnt = board[ran]
            # 방문하지 않았을때 추가
            if visited[cnt] == 0:
                q.append(cnt)
                visited[cnt] = visited[target] + 1
                # 100번째 칸까지 탐색했으면 리턴
                if cnt == 100:
                    return
# 입력
n, m = map(int, input().split())    # n(사다리의 수), m(뱀의 수)
board = [i for i in range(101)] # 보드판
visited = [0] * 101 # 주사위 횟수 저장
# 보드에 사다리, 뱀 추가
for _ in range(n+m):
    x, y = map(int, input().split())
    # 두번째칸이 사다리나 뱀 이동위치
    board[x] = y
# bfs 진행
bfs(1)
# 출력 
print(visited[100])

# 피드백
# 구현,완전 탐색 실패(테케만 맞음) -> bfs 풀이