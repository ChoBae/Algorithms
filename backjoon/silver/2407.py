# 조합 실버4
# nCm 출력 (조합)
# 팩토리얼 함수
def fac(n):
    r = 1
    for i in range(2, n+1):
        r *= i
    return r
# 입력
n, m = map(int, input().split())
# 정답
answer = fac(n)//(fac(m)*fac(n-m))
print(answer)