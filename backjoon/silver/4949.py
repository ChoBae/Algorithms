# 균형잡힌 세상
answers = []    # 정답
while True:
    # 변환값
    stack = []
    check = True
    # 출력
    tmp = input()
    # 종료 조건
    if tmp == '.':
        break
    # 솔루션
    for stacks in tmp:
        if stacks == '(' or stacks == '[':
            stack.append(stacks)
        # ')'가 들어왔을 경우
        elif stacks == ')':
            # 스택에 처음일때와 '['일때 오류
            if not stack or stack[-1] == '[':
                check= False
                break
            # 스택에 마지막이 '('일땐 뺴주기
            if stack[-1] == '(':
                stack.pop()
            # 아니면 오류

        # ')'가 들어왔을 경우
        elif stacks == ']':
            # 스택에 처음일때와 '(' 일때 오류
            if not stack or stack[-1] == '(':
                check= False
                break
            # 스택에 마지막이 '['일땐 뺴주기
            if stack[-1] == '[':
                stack.pop()
    # 결과 넣어주기
    if check and not stack:
        answers.append('yes')
    else:
        answers.append('no')
# 출력        
for answer in answers:
    print(answer)