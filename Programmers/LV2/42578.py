# 위장
from itertools import combinations
def solution(clothes):
    answer = 0
    # 한옷 조합 두옷 조합.
    for i in range(1,len(clothes)+ 1):
        com = list(combinations(clothes, i))



        for coms in com:
            result = []
            for i in coms:
                nextType = i[1]
                if nextType not in result:
                    result.append(nextType)
                    if len(result) == i:
                        answer += 1
                        break
    print(answer)
    return answer


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
#,["black jean", "bottom"], ["hood", "top"]