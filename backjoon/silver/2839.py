# 설탕배달 브론즈1
n = int(input())    # 설탕 n(kg)
answer = 0  # 정답 
while n >= 0:
    # 5로 나누어지면 저장값에 몫만큼 더하고 출력.
    if n % 5 == 0:
        answer += n //5
        print(answer)
        break
    # 5로 나누어지지 않다면 3를 빼줌
    n -= 3
    answer += 1
# while이 false라면 -1
else:
    print(-1)