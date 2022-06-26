# 대소문자 
def solution(s):
    slists = s.split(" ") # 공백이 두개일때 추가해줘야함..
    answer = []
    for slist in slists:
        answer.append(slist.lower().capitalize())
    print(answer)
    return " ".join(answer)

solution('aaaaa  a  aa  ')