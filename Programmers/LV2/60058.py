# 2020 카카오 블라인드 '괄호 변환' -> 풀었다..

# 솔루션
def solution(p):
    p = list(p) # p 변경 쉽게 리스트화
    global answer
    answer = ''
    # 해당 p 괄호변환 시작
    recu(p)
    print(answer)
    return answer

# u가 올바른 괄호 문자열인지 확인하는 함수
def check(u):
    # 시작이 ")"이면 올바른 문자열이 아님
    if u[0] == ')':
        return False
    else:
        st = []
        for i in range(len(u)):
            if len(st) >=1:
                if st[-1] == "(" and u[i] == ')':
                    st.pop()
                    continue        
            st.append(u[i])
            
        if not st:
            return True
        else:
            return False
             
            
# 괄호 변환 함수
def recu(w):
    global answer   # answer 전역변수 적용
    # 빈문자열일때 재귀 종료
    if len(w) == 0:
        return w  # 빈 문자열일때 빈문자열반환
    else:
        u = []  
        state = 0   # 균형잡힌 괄호 문자열을 찾기 위한 카운트 변수값
        # w빌때까지 반복
        while w:
            # w의 앞부터 u에 넣어주기
            now = w.pop(0)
            u.append(now)
            # 균형잡힌지만 체크하기 위해서 간단하게 +1 , -1 로만 검사?
            if now == '(':
                state += 1
            else:
                state -= 1
            # 만약 state가 0이 된거면 균형잡힌 괄호 문자열인 것.
            if state == 0:
                # 남은 w가 -> v
                v = w
                print(u, v)

                # u가 '올바른 괄호 문자열' 일때
                if check(u):
                    answer = ''.join(u) + ''.join(recu(v))
                    return answer
                # u가 '올바른 괄호 문자열'이 아닐때
                else:
                    # 주어진 과정처럼 문자열 더해주기
                    u = u[1:-1]
                    for i in range(len(u)):
                        if u[i] == '(':
                            u[i] = ')'
                        else:
                            u[i] = "("
                    answer = "(" + ''.join(recu(v)) + ")" + ''.join(u)
                    return answer
                    # 남은 v를 다시 재귀 처리
                    
    return w
solution("()))((()")
solution(")()(()")
