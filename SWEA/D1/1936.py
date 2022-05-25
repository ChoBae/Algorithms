# 1대1 가위바위보
a, b = map(int, input().split())
if (a == 3 and b == 2) or (a == 2 and b == 1) or (a == 1 and b == 3) :
    print("A")
else:
    print("B")
