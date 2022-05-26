# 숫자를 정렬하자
t = int(input())
for tc in range(1, t+1):
    # 입력
    n = int(input())
    numLi = list(map(int, input().split()))
    numLi.sort()    # 오름차순 정렬
    # 출력
    print(f"#{tc}", end=' ')
    print(*numLi)
