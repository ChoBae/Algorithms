# 햄버거 다이어트
# 경우의수 처리 combinations 모듈
from itertools import combinations
ts = int(input())
for tc in range(1, ts + 1):
    # 입력
    n, l = map(int, input().split())
    li = [0] * n    # 재료 리스트
    answer = 0  # 정답
    # 재료 리스트 생성
    for i in range(n):
        t, k = map(int, input().split())
        li[i] = (t, k)
    # 1~5가지 조합의 재료 경우의수 구하기
    for i in range(1, n+1):
        comb = list(combinations(li, i))
        # 해당 경우의 수 별 재료 총 칼로리, 만족도 합 구하기
        for com in comb:
            totta, totca = 0, 0
            for tas, cal in com:
                totta += tas
                totca += cal
            # 이번 경우의수에서 총칼로리가 제한 칼로리에 만족할때 최대값 업데이트
            if totca <= l:
                answer = max(answer, totta)
    print(f"#{tc} {answer}")
