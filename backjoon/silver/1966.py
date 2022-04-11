# 프린터 큐 실버3 구현, 큐구조?
# 입력
t = int(input())    # 테스트 케이스 수
answers = []    # 답
start = 0   # 인덱스 값
# 테스트 케이스 체크
for i in range(t):
    # n(문서의 개수), m(문서의 위치(인덱스))
    n, m = map(int, input().split())
    # numLi 받고, 인덱스랑 묶어서 변환
    numLi = list(map(int, input().split()))
    for i in range(len(numLi)):
        numLi[i] = (i, numLi[i])
    target = numLi[m]   # 해당 위치의 숫자
    numLen = len(numLi) # 숫자 리스트 길이 -> 몇번째로 나갔는지 체크
    
    while True:
        check = True    # 숫자 검사 boolean
        tmp = numLi.pop(0)  # 첫번째순서의 값 pop
        start += 1  # 인덱스 더해주기
        # 남은 숫자리스트 검사
        for num in numLi:
            # 큰 수가 있으면 false
            if num[1] > tmp[1]:
                check = False
                break
        # 큰수가 있을때 pop해준 값 다시 넣어주기
        if not check:
            numLi.append(tmp)
        # 큰수가 없고, tmp가 target 값일때
        if check and target == tmp:
            answers.append(numLen-len(numLi))
            break
# 출력
for answer in answers:
    print(answer)