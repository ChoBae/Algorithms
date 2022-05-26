# 시각 덧셈
t= int(input())
for tc in range(1, t+1):
    # 입력
    firMin, firSec, secondMin, secondSec = map(int, input().split())
    resultMin = firMin + secondMin if firMin + secondMin <= 12 else firMin + secondMin - 12
    resultSec = firSec + secondSec
    # 60분이 넘었으면 시간 + 1
    if resultSec > 60:
        resultSec -= 60
        resultMin += 1
    # 출력
    print(f"#{tc} {resultMin} {resultSec}")
    