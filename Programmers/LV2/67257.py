# 수식 최대화

from itertools import permutations

def solution(expression):
    act = ['*', '+', '-']
    answer = []
    # 연산 경우의 수 리스트 생성
    comAct = list(permutations(act,3))
    
    for act in comAct:
        last = act[0]  # 우선순위가 가장 마지막인
        second = act[1] # 우선순위가 두번째인 연산
        tmpLi = []  # 저장 값
        # 우선순위가 마지막인 연산을 기준으로 나눠줌
        # *, +, - 순서일때 "100-200*300-500+20"일때
        # 100, 200*300, 500+20
        for i in expression.split(last):
            # 100 -> 200*300 -> 500+20 순서
            # 우선순위가 두번째인 연산(+)을 기준으로 나누며 ()안에 넣어주며 tmp 리스트에 넣어줌
            # 100, 200*300 두번째 연산 기준으로 나눌 수없으므로 바로 tmpLi = [(100),(200*300)]
            tmp = [f"({j})" for j in i.split(second)]
            # 500+20 은 나눌 수 있으므로 tmp = [(500),(20)] -> tmpLi = [(100),(200*300),((500)+(20))]
            tmpLi.append(f"({second.join(tmp)})")
        # eval를 이용 문자열을 연산해주고, abs를 이용하여 절대값 처리해줌.
        # tmpLi의 값들을 우선순위가 마지막 연산을 연결시켜줌.
        # ((100))-((200*300))-((500)+(20)) -> 자연스럽게 순서대로 처리가 가능해짐.
        answer.append(abs(eval(last.join(tmpLi))))
    return max(answer)



solution("100-200*300-500+20")