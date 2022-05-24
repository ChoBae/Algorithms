# 지그재그 숫자
t = int(input())
for tc in range(1, t+1):
    # 입력
    num = int(input())
    result = 0  # 정답
    # num의 수만큼 반복
    for i in range(1,num+1):
        # 짝수일때 빼기
        if i % 2 == 0:
            result -= i
        # 홀수일때 더하기
        else:
            result += i
    # 출력
    print(f"#{tc} {result}")