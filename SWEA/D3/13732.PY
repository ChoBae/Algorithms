# 정사각형 판정
# 입력
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    maps = []   # 맵리스트
    answer = True  # 정답 판별 불린형
    # 맵 입력
    for i in range(n):
        maps.append(list(input()))
    # '#' 위치(인덱스) 찍기
    tmp = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] == '#':
                tmp[i].append(j)
    res = []    # 빈 공간 제외한 리스트
    # 빈공간 제외하기
    for row in tmp:
        if len(row) > 0:
            res.append(row)
    # #이 없거나, 
    if len(res) != len(res[0]) or len(res) == 0:
        answer = False
    else:
        if len(res) != 1:
            for i in range(1, len(res)):
                if res[i] != res[i-1]:
                    answer = False
                    break

    if answer:
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")
