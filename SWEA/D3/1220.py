# Magnetic
t = 10  # 이거에서 많이 틀리실듯 ㅠㅠ
# 정답 리스트
answers = []
for tc in range(1, t+1):
    n = int(input())    # n x n의 테이블
    table = [list(map(int, input().split())) for _ in range(n)]  # 테이블 생성
    ans = 0  # 정답 카운트
    # 1은 n극 , 2는 s극
    for i in range(n):
        tmp = ''    # 해당 열 저장 변수
        # 테이블 생성
        for j in range(n):
            if table[j][i] != 0:
                tmp += str(table[j][i])
        startIdx, endIdx = -1, 101  # 시작 idx, 끝 idx (자기장에 버려지는 과정)
        for z in range(len(tmp)):
            # 첫번째 1이 시작 인덱스(1은 밑으로 떨어지려하므로)
            if tmp[z] == '1' and startIdx < 0:
                startIdx = z
            # 마지막 2가 끝 인덱스 (2는 위로 떨어지려하므로)
            if tmp[z] == '2':
                endIdx = z
        step, cnt = 0, 0
        for state in tmp:
            # 112, 122 같은 변수가 있을때 하나로 계산하기 위한 변수
            # 1 ->2 가 나올때 카운트
            if state == '1' and step == 0:
                step += 1
            if state == '2' and step == 1:
                step = 0
                cnt += 1
        ans += cnt  # 카운트 업데이트
    # 정답 리스트에 넣어주기
    answers.append(ans)
# 출력
for i in range(1, t+1):
    print(f"#{i} {answers[i-1]}")
