# 1269 대칭 차집합
# 이렇게 
alen, blen = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
result = len(a - b) + len(b - a)
print(result)