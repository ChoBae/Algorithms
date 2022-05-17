# view
# 입력
T = int(input())
for test_case in range(1, T + 1):
    width = int(input())    # 가로길이
    buildings = list(map(int, input().split())) # 빌딩 입력
    result = 0 # 결과 값 초기화
    # 가로 길이(빌딩 수) 만큼 체크
    for i in range(2, width):
        nowHeight = buildings[i] # 현재 빌딩의 높이
        # 현재 빌딩에서 1~2번째 앞뒤 체크
        if nowHeight > buildings[i-2] and nowHeight > buildings[i-1] and nowHeight > buildings[i+1] and nowHeight > buildings[i+2]:
            # 그 중 가장 높은 값 구하기
            maxHeight = max(buildings[i-2], buildings[i-1],
                            buildings[i+1], buildings[i+2])
            # 결과값 업데이트
            result += nowHeight - maxHeight
    print(f"#{test_case} {result}")