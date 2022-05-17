# 간단한 369게임
# 입력
N = int(input())
# 솔루션
for i in range(1, N+1):
    # 3,6,9가 들어가있는 숫자일때
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = 0 # 카운트
        for st in str(i):
            # 3,6,9가 몇개 들어가있는지 확인
            if st == '3' or st == '6' or st == '9':
                cnt += 1
        print(cnt*'-', end=' ')
    # 3,6,9가 안들어있다면 바로 출력
    else:
        print(i, end=' ')
