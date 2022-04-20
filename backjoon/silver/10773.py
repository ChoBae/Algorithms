# 제로
# 입력
k = int(input())
numLi = []
# 솔루션
for _ in range(k):
    tmp = int(input())
    # 0일때 가장 최근의 수 빼기
    if tmp == 0:
        numLi.pop()
        continue
    # 0이 아닐때 리스트에 넣어주기
    numLi.append(tmp)
# 출력
print(sum(numLi))
    
    