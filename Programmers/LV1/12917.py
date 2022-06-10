# 문자열 내림차순으로 배치하기
def solution(s):
    tmp = list(s)
    tmp.sort(reverse=True)
    return ''.join(tmp)
solution("Zbcdefg")