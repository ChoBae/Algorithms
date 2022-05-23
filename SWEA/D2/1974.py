# 스도쿠 검증
t = int(input())
for tc in range(1,t+1):
    maps = [list(map(int,input().split())) for _ in range(9)] # 맵 데이터
    check = True    # 스도쿠 가능 여부 확인 boolean
    # 맵 좌표(i, j) -> 가로, 세로 스도쿠 체크
    for i in range(9):
        tmp, tmp2 = {} , {} # 행, 열 스도쿠 확인 딕셔너리
        for j in range(9):
            num = maps[j][i]    # 열
            num2 = maps[i][j]   # 행
            if num not in tmp:
                tmp[num] = 1
            # 중복이 나올때 스도쿠 불가
            else:
                check = False
                break
            if num2 not in tmp2:
                tmp2[num2] = 1
            # 중복이 나올때 스도쿠 불가
            else:
                check = False
                break
    # 맵 좌표(i, j) -> 9칸 스도쿠 확인
    for i in range(0,9,3):
        for j in range(0,9,3):
            # 좌표가 0,0 -> 0,3 -> 0,6... 3,0 -> 3,3 -> 3,6 . 이런식으로 9칸씩 확인
            result = maps[i][j:j+3] + maps[i+1][j:j+3] + maps[i+2][j:j+3]
            # set으로 중복제거한 뒤 9개가 아닐때(같은 수가 있을때) 스도쿠 불가
            if len(set(result)) !=9:
                check = False
                break
    # 출력
    if check:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")