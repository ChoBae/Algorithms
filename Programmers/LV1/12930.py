# 이상한 문자 만들기
def solution(s):
    s = s.lower().split(" ")
    return ' '.join([ ''.join([ x.upper() if i % 2 == 0 else x for i, x in enumerate(w)]) for w in s]) 
solution("try hello world")