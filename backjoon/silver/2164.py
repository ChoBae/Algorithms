# 카드2 실버4
n = int(input())
cardLi = [i+1 for i in range(n)]

while len(cardLi) != 1:
    # 카드를 땅에 버림
    cardLi.pop(0)
    # 카드를 꺼내서 맨밑으로 넣음
    setCard = cardLi.pop(0)
    cardLi.append(setCard)


print(cardLi[0])
