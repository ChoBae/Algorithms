# 새로운 불면증 치료법
t = int(input())
for tc in range(1,t+1):
    # 입력
    n = int(input())
    result = []
    step = 1
    while len(result) != 10:
        tmp = n * step
        step += 1
        for st in str(tmp):
            if st not in result:
                result.append(st)
        
    print(f"#{tc} {tmp}")
                