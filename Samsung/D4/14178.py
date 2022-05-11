# 1차원 정원
t = int(input())
# for i in range(t):
#     cnt = 0
#     n, d = map(int, input().split())
#     for j in range(d+1, n+1, (d*2) +1 ):
#         set = i + d
#         cnt+= 1
#         print(i)
#     if set < n:
#         print(f"#{i+1} {cnt+1}")
#     else:
#         print(f"#{i+1} {cnt+1}")
for t in range(1, T + 1):
    N,D=map(int,input().split())
    value=N // ((2 * D) + 1)

    if N%((2*D)+1)>0:
        value+=1

    print(f"#{t} {value}")