# 11728 배열 합치기
import sys
input = lambda:sys.stdin.readline().rstrip()
# 기본 풀이
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# result = a + b
# result.sort()
# print(*result);


# 투포인터 풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

aP, bP = 0, 0
result = []
while aP != n or bP != m:
    if aP == n:
        result.append(b[bP])
        bP += 1
    elif bP == m:
        result.append(a[aP])
        aP += 1
    else:
        if a[aP] < b[bP]:
            result.append(a[aP])
            aP += 1
        else:
            result.append(b[bP])
            bP += 1
print(*result)
