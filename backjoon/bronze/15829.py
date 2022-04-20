# 해싱
# 입력
l = int(input())
alp = input()
li = []
# 해싱 초기값
hashCount = 31
# 솔루션
for i in range(l):
    cnt = hashCount ** i
    li.append((ord(alp[i])-96) * cnt)
# 출력   
print(sum(li)%1234567891)