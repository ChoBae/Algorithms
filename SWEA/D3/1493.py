# 수의 새로운 연산
t = int(input())

for tc in range(1, t+1):
    p, q = map(int, input().split())
    ng, count = 1, 0
    maps = [[0] * q for _ in range(q)]
    while True:
        for i in range(1, ng):
            # 짝수 일때
            if ng % 2 == 0:
                count += 1

        ng += 1
