# 간단한 소인수 분해
t = int(input())
result = [2, 3, 5, 7, 11]
for tc in range(1, t+1):
    n = int(input())
    print(f"#{tc}", end= ' ')
    for i in result:
        cnt = 0
        while True:
            if n % i == 0:
                n = n//i
                cnt +=1
            else:
                break
        # 출력
        print(cnt, end= ' ')

