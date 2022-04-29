# 패션왕 신해빈 실버3
# import sys
# from itertools import combinations
# input = sys.stdin.readline
# t = int(input())
# clothes = []

# for _ in range(t):
#     for _ in range(int(input())):
#         name, type = map(str, input().split())
#         clothes.append((name, type))
# answer = len(clothes)

# for i in range(2, len(clothes) + 1):
#     comb = list(combinations(clothes,i))
#     for com in comb:
#         tmp = []
#         for n, t in com:
#             # 해당 타입의 옷을 이미 착용했을때
#             if t not in tmp:
#                 tmp.append(t)
                
#         if len(tmp) == i:
#             answer += 1
        
#     print(answer)

### 시간초과
import sys
input = sys.stdin.readline
# 입력
t = int(input())
for _ in range(t):
    clothes = {}
    for _ in range(int(input())):
        name, type = map(str, input().split())
        if type in clothes:
            clothes[type].append(name)
        else:
            clothes[type] = [name]
    count = 1   # 초기값
    # 경우의수 구하기
    for cloth in clothes:
        count *=(len(clothes[cloth])+1)
    # 출력
    print(count-1)
