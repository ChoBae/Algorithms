# 분해합 브론즈2
# 입력
n = int(input())
answer = 1000000
# 솔루션 
for i in range(1,1000000):
    tmp = i
    # 자리수마다 더하기
    for tmps in str(tmp):
        tmp +=int(tmps)
    # 타겟수랑 같을때 갱신
    if tmp == n:
        answer = min(answer, i)
# 출력
if answer == 1000000:
    print(0)
else:
    print(answer)