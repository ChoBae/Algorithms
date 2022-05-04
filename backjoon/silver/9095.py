# 1,2,3 더하기 실버3
import sys
from itertools import product
input = sys.stdin.readline
# 입력
numbers = [1,2,3]
answers = []
t = int(input())
# 솔루션
for _ in range(t):
    num = int(input())
    # 카운트 초기화
    count = 0
    # product 함수 사용
    for i in range(1,num+1):
        coms = list(product(numbers,repeat = i))
        # 해당 개수의 수의 경우의 수에서 탐색
        for com in coms:
            if sum(com) == num:
                count += 1
    # 정답 추가
    answers.append(count)

# 출력
for answer in answers:
    print(answer)
