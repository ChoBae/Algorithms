# 어디에 단어가 들어갈 수 있을까
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())    # n x n 의 맵, k (타겟 수)
    maps = [list(map(int, input().split())) for _ in range(n)] # 맵 데이터 생성
    result = 0 # 답
    # 행 검사
    for i in range(n):
        cnt = 0 # 1의 개수를 카운트
        # 행 별로 검사
        for state in maps[i]:
            # 1이 나왔을때 카운트
            if state == 1:
                cnt += 1
            # 카운트 되고있을때 0이 나온다면 cnt 초기화 -> 그전에 cnt가 타겟값이라면 답 업데이트
            if cnt !=0 and state == 0:
                if cnt == k:
                    result += 1
                cnt = 0
        # 답 업데이트
        if cnt == k:
            result += 1
    # 열 검사
    for i in range(n):
        tmp ='' # 열 데이터
        cnt = 0 # 1의 개수를 카운트
        # 열 데이터 생성 
        for j in range(n):
            tmp += str(maps[j][i])
        # 해당 열 검사
        for state in tmp:
            # 1이 나왔을때 카운트
            if state == '1':
                cnt += 1
            # 카운트 되고있을때 0이 나온다면 cnt 초기화 -> 그전에 cnt가 타겟값이라면 답 업데이트
            if cnt !=0 and state == '0':
                if cnt == k:
                    result += 1
                cnt = 0  
        # 답 업데이트  
        if cnt == k:
            result += 1
    # 출력    
    print(f"#{tc} {result}")