answer = ''
def check(u):
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
             
            

def recu(w):
    global answer
    if len(w) == 0:
        return w    # 빈 문자열일때 빈문자열반환
    else:
        u = []
        state = 0
        while w:
            now = w.pop(0)
            u.append(now)
            if now == '(':
                state += 1
            else:
                state -= 1
        
            if state == 0:
                v = w
                print(u, v)
                if check(u):
                    if not v:
                        answer += ''.join(u)
                    else:
                        answer += ''.join(u)
                        tmp = recu(v)
                else:
                    u = u[1:-1]
                    for i in range(len(u)):
                        if u[i] == '(':
                            u[i] = ')'
                        else:
                            u[i] = "("
                    print(u)
 
                    res = "(" + ''.join(u) + ")" + recu(v)
                    print(res)
    return u
         
def solution(p):
    p = list(p)
    u = []
    state = 0
    # 주어진 p를 모두 변환할때까지
    print(recu(p))
    return answer
solution("()))((()")