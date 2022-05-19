# N-Queen 백트래킹
# # 입력
# T = int(input())
# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         ans += 1
#         print(ans)
#         return
#     else:
#         for i in range(n):
#             row[x] = i
#             print(row)
#             if is_promising(x):
#                 n_queens(x+1)

# for test_case in range(1, T + 1):
#     n = int(input())
#     ans = 0
#     row = [0] * n
#     n_queens(0)
#     print(ans)


# 다시풀기
# 퀸이 놓을 수 있는 지 체크 함수
def check(states):
    # 같은 열에 있는지, 대각선에 있는지 체크
    for state in range(states):
        if row[states] == row[state] or abs(row[states] - row[state]) == abs(states - state):
            return False
    return True

# 백트래킹 솔루션
def backtracking(num):
    global result
    # 백트래킹 과정에서 퀸이 목표 개수만큼 놓았을때 백트래킹
    if num == n:
        result += 1
        return
    # 퀸 놓기
    else:
        for i in range(n):
            row[num] = i    # 현재 열에 i번째 자리에 퀸을 놓았다는 뜻
            # 현재 열에 퀸을 놓을수 있을때 다음 열로
            if check(num):
                backtracking(num+1)


T = int(input())
for tc in range(1, T+1):
    # 입력
    n = int(input())    # n x n 의 맵, 퀸의 수
    row = [0] * n  # 각 열의 퀸의 현재 위치(인덱스)
    result = 0
    backtracking(0)  # 0 부터 시작.
    # 출력
    print(f"#{tc} {result}")
