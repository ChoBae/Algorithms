# 카드2 실버4
from collections import deque
# n = int(input())
# cardLi = [i+1 for i in range(n)]
# cardLi = deque(cardLi)
# while len(cardLi) != 1:
#     # 카드를 땅에 버림->pop보다 더 시간복잡도가 좋네
#     # 리스트에서 pop(0)으로 가장 앞단의 값을 꺼낼때 list크기만큼 시간이 걸린다(O(n))
#     # 하지만 deque에서 popleft()의 경우 똑같은 pop(0)인데 O(1)의 시간복잡도.
#     # -> index값을 알경우에는 결국 똑같긴하다.
#     cardLi.popleft()
#     # 카드를 꺼내서 맨밑으로 넣음
#     setCard = cardLi.popleft()
#     cardLi.append(setCard)
# print(cardLi[0])

# 인덱스로 뺄경우 ->시간초과
n = int(input())
cardStr = ''
for i in range(n):
    cardStr += str(i+1)
while len(cardStr) != 1:
    # 첫번째제거
    cardStr = cardStr[1:]
    # 그이후오는수 뒤로빼기
    setCard = cardStr[0]
    cardStr = cardStr[1:] + setCard
print(cardStr)

