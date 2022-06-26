# 괄호 회전하기
# 괄호 체크 함수
def check(sl):
    temp = []
    sl = list(sl)
    while sl:
        now = sl.pop(0)
        if len(temp) >= 1:
            if temp[-1] == '(' and now == ')':
                temp.pop()
            elif temp[-1] == '[' and now == ']':
                temp.pop()
            elif temp[-1] == '{' and now == '}':
                temp.pop()
        else:
            temp.append(now)
    # temp가 비어야지 괄호가 맞았던것        
    if not temp:
        return True
    else:
        return False
# 솔루션 함수
def solution(s):
    answer = 0
    # 해당 길이만큼 s 문자열 변환
    for i in range(len(s)):
        # 괄호가 맞는지 확인
        if check(s):
            answer += 1
        # s문자열 변환
        s = s[1:] + s[0]
    print(answer)
    return answer
solution("[)(]")