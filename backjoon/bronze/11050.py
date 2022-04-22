# 이항계수 -> 수학적인 문제
from sys import stdin
# 팩토리얼 함수
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n, k = map(int, stdin.readline().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))