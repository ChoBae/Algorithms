# 준환이의 운동관리
t = int(input())
for tc in range(1, t+1):
    l, u, x = map(int, input().split())
    if l > x:
        result = l-x
    elif u < x:
        result = -1
    else:
        result = 0
    # 출력
    print(f"#{tc} {result}")