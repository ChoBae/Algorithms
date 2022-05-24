# 알파벳을 숫자로 변환
a = input()
for i in range(len(a)):
    print(ord(a[i])-64,end=' ')