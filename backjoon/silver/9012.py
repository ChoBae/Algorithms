# 괄호 실버4 
# 인풋
t = int(input())    # 테스트케이스 수
answers = []    # 답안

# 솔루션
for i in range(t):
    tmp = input()   # 입력값
    stack = []  # 스택
    # 첫번째로 ')'가 들어오면 오류 
    if tmp[0] == ')':
        answers.append('NO')
    else:
        # 스택에 하나씩 넣어주면서 체크
        for tmps in tmp:
            stack.append(tmps)   
            # 스택에 쌓인게 2개 이상일때 검사
            if len(stack) >=2:
                # 마지막과 그앞을 확인해서 VPS('()')라면 빼줌.
                # 단 ')(' 방지로 앞의 값이 '('일 경우를 추가해줌
                if stack[-1] != stack[-2] and stack[-2] =='(':
                    stack.pop()
                    stack.pop()
        # 체크를 마쳤을때 스택에 남아있으면 NO 아니면 YES
        if len(stack) == 0:
            answers.append('YES')
        else:
            answers.append('NO')
# 출력
for answer in answers:
    print(answer)
