# 농작물 수확하기
T = int(input())
for tc in range(1, T+1):
    # 입력
    n = int(input())
    maps = [list(input()) for _ in range(n)]    # map 데이터
    startLen = 0 # 숫자 범위
    mid = len(maps) // 2    # 중앙 위치 값
    result = 0  # 결과값
    # 마름모 윗부분
    for i in range(mid+1):
        tmp = maps[i][mid-startLen: mid+startLen+1]
        result += sum(list(map(int, tmp)))
        startLen += 1
    # 윗부분이 끝나고 -1 해줘야함
    startLen -= 1
    # 마름모 아랫부분
    for i in range(mid+1, n):
        startLen -= 1
        tmp = maps[i][mid-startLen: mid+startLen+1]
        result += sum(list(map(int, tmp)))
    # 출력
    print(f"#{tc} {result}")
