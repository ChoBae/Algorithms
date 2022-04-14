# 수 정렬하기2
import sys
input = sys.stdin.readline
# 입력
n = int(input())
answers = []
for _ in range(n):
    answers.append(int(input()))
# 정렬
answers.sort()
# 출력
for answer in answers:
    print(answer)