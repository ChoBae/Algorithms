# 원재의 메모리 복구하기
t = int(input())
for tc in range(1, t+1):
    st  = input() # 입력
    start = ['0'] * len(st) # 시작 비트
    answer = 0  # 정답 
    # 입력값 만큼 반복
    for i in range(len(st)):
        # 시작비트와 비교했을떄 같으면 pass
        if st[i] == start[i]:
            pass
        # 시작비트와 다를때
        else:
            # 카운트 업데이트
            answer += 1
            # 그 이후값 현재 비트 값으로 변환
            for j in range(i,len(st)):
                start[j] = st[i]
    # 출력
    print(f"#{tc} {answer}")