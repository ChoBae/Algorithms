# AC 골드5
t = int(input())
results = []
for _ in range(t):
    p = input()     # 함수 R(뒤집기), D(버리기)
    n = int(input())    # x 길이
    # x 리스트화 -> '입력시 []가 들어와서 빼고 리스트화'
    xlists = input()
    x = xlists[1:-1].split(',')
    # n이 0일때 -> 빈 x
    if n == 0:
        x = []
    # 연산 진행 및 에러 체크
    error, rvs = False, False
    for state in p:
        # R(뒤집기) 진행
        if state == 'R':
            rvs = not rvs
        # D(버리기) 진행
        elif state == 'D':
            if len(x) < 1:
                error = True
                break
            else:
                if rvs:
                    x.pop()
                elif not rvs:
                    x.pop(0)
    # 에러가 있을때나, 남은 x의 길이가 0일때 error를 결과값 리스트에 넣어줌
    if error:
        results.append("error")
    # x가 구해졌을때 -> str형으로 변환 후 결과값 리스트에 넣어줌
    else:
        if rvs:
            x = x[::-1]
        results.append("[" + ",".join(x)+"]")
# 결과값 출력
for result in results:
    print(result)