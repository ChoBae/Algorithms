# 부분 수열의 합
# combinations 모듈 사용풀이 -> 시간초과
# from itertools import combinations
# t = int(input())
# for tc in range(1, t+1):
#     n, k = map(int, input().split())    # a(배열의 길이), k(타겟 수)
#     a = list(map(int,input().split()))  # 배열
#     result = 0  # 결과값
#     # 경우의수
#     for i in range(1,len(a)+1):
#         comb = list(combinations(a,i))
#         for com in comb:
#             if sum(com) == k:
#                 result += 1
#     # 출력
#     print(f"#{tc} {result}")
# 재귀 사용 풀이 -> 통과
def solve(idx, sum):
    global result
    # 재귀 중지 -> 배열의 길이를 초과했을때
    if idx >= n:
        return
    tmp = sum + a[idx]
    # 타겟 수가 되었을때
    if tmp == k:
        result += 1
    # 재귀
    # 현재 인덱스만 더한값
    solve(idx+1, sum)
    # 현재 인덱스와 이전 인덱스의 값을 모두 더한 값
    solve(idx+1, tmp)


t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())    # a(배열의 길이), k(타겟)
    a = list(map(int, input().split()))  # 배열
    result = 0  # 결과값
    solve(0, 0)  # 파라미터값 인덱스, sum(현재 경우의 합)
    # 출력
    print(f"#{tc} {result}")
