# 동전 골드5
t = int(input())    # 테스트 케이스 입력
for _ in range(t):
    # 입력
    n = int(input())    # 화폐 단위 갯수
    pays = list(map(int, input().split()))  # 화폐 단위
    target = int(input())   # 찾으려는 값 
    # 다이나믹 프로그래밍 
    d = [0] * (target+1)
    d[0] = 1    # 초기값 설정
    # 화폐 단위별로 구하기
    for pay in pays:
        for i in range(target+1):
            # 현재 i 값이 현재 화폐단위로 구할 수 있을때
            if i >= pay:
                # 현재 d값에 *현재의 화폐값을 제외한 값*을 구할 수 있었던 경우의 수를 더 해준다.
                d[i] += d[i - pay]
    # 출력
    print(d[target])    
    