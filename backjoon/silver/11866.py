# 요세푸스 문제
from collections import deque
# 입력
n, k = map(int, input().split())
numLi = [i+1 for i in range(n)]
answers = []
# 솔루션
# 수를 다 찾을때 까지
numLi = deque(numLi)
while numLi:
    for _ in range(k-1):
        numLi.append(numLi.popleft())
    answers.append(numLi.popleft())
# 출력
print("<", end="")
# join을 사용해서 사이에 ', '를 넣어준다.
# join을 통해 문자열을 합칠때 문자형이여야해서 map으로 str로 전환해줬다.
answer = ', '.join(map(str,answers))
print(answer, end="")
print(">")