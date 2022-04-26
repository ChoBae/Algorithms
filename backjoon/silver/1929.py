# 소수 구하기
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
# # 솔루션 소수 함수
# def sosu(num):
#     if num <= 2:
#         return False
#     mid = int(num**0.5)
#     for i in range(2,mid+1):
#         if num % i == 0:
#             return False
#     return True
# 에라스토테네스의 체
# 2,3,4....의 배수들을 지워나가는 알고리즘
n += 1
sieve = [True] * n

mid = int(n ** 0.5)
for i in range(2, mid+1):
    if sieve[i]:
        for j in range(2*i, n, i):
            sieve[j] = False

for i in range(m, n):
    if i > 1 and sieve[i] == True:
        print(i)