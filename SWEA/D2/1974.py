# 스도쿠 검증
t = int(input())
for tc in range(1,t+1):
    maps = [list(map(int,input().split())) for _ in range(9)] # 맵 데이터
    check = True
    for i in range(9):
        tmp = {}
        for j in range(9):
            num = maps[j][i]
            if num not in tmp:
                tmp[num] = 1
            else:
                tmp[num] += 1
                check = False
                break
            
    for i in range(0,9,3):
        for j in range(0,9,3):
            result = maps[i][j:j+3] + maps[i+1][j:j+3] + maps[i+2][j:j+3]
            if len(set(result)) !=9:
                check = False
                break
             
    if check:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")