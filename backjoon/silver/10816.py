# 숫자카드 2
# 입력
n = int(input())
numLi = list(map(int, input().split()))
m = int(input())
mnumLi = list(map(int, input().split()))
# 딕셔너리 저장
dict = {}
for num in numLi:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
# 딕셔너리 밸류값 찾아 출력
for mnum in mnumLi:
    if dict.get(mnum) == None:
        print(0, end= " ")
    else:
        print(dict.get(mnum), end= " ")