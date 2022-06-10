# 최대 공약수와 최소 공배수
# math 라이브러리 사용 풀이 3.8버전은 안됨.
# from math import gcd, lcm
# def solution(n, m):
#     answer = [0] * 2
#     answer[0] = gcd(n,m)
#     answer[1] = lcm(n,m)
#     return answer
# 각각 함수화로 풀이
# 최대공약수 구하기
def gcd(n,m):
    if n < m:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n
# 최소 공배수 구하기
def lcm(n,m):
    nlist = [i * n for i in range(1, m+1)]
    mlist = [i * m for i in range(1, n+1)]
    # set은 &로 교집합을 구할 수 있다.
    result = list(set(nlist) & set(mlist))
    return min(result)
# 출력
def solution(n, m):
    answer = [0] * 2
    answer[0] = gcd(n, m)
    answer[1] = lcm(n, m)
    return answer
solution(2,5)