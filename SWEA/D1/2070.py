# 큰놈, 작은놈, 같은 놈
t = int(input())
for tc in range(1, t+1):
    x, y = map(int, input().split())
    result = ''
    if x < y:
        result = '<'
    elif x > y:
        result = ">"
    else:
        result = "="
    print(f"#{tc} {result}")