# 요세푸스 문제
n, k = map(int, input().split())
numLi = [i+1 for i in range(n)]
answers = []
answer = ''
state = 0
# 솔루션
# 수를 다 찾을때 까지
while numLi:
    state += k

    if state > len(numLi):
        state -=  len(numLi)
        
    if state > len(numLi):
        state -=  len(numLi)
        
    

    if numLi[state-1] not in answers:
        answers.append(str(numLi[state-1]))
        answer += str(numLi[state-1])
        numLi.remove(numLi[state-1])
        state -= 1

result =', '.join(answers)
print("<"+result+">")
