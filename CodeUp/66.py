# 블럭 탑쌓기

# tower = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
# rule = "ABD"
# ing = []
# result = []

# #전체블록 -> 부분블록 체크
# for towers in tower:
#     #규칙 A-B-D 반복
#     for rules in rule:
#         # 만약 부분블록안에 규칙이 있으면
#         if rules in towers:
#             # 부분블록의 문자 하나씩
#             for num in towers:
#                 # 문자랑 규칙과 같으면 해당의 인덱스를 넣어줌
#                 if rules == num:
#                     ing.append(towers.index(num))
#     #규칙을 체크하는 반복이 끝나고 오름차순으로 정렬되어있다면 '가능' 아니면 '불가능'
#     if ing == sorted(ing):
#         ing.clear()
#         result.append('가능')
    
#     else:
#         ing.clear()
#         result.append('불가능')

# print(result)

# ------------------------------------- 답안--------------------------------------------
# 결과값 함수
def sol(tower, rule):
    result = []
    for towers in tower:
        result.append(check(towers, rule))
    return result

# 내장 체크 함수
def check(towers, rule):
    #인덱스를 비교할 변수 -> 0부터
    sorting = rule.index(rule[0])
    for towers_word in towers:
        if towers_word in rule:
            # A->B->D의 순으로 되야하기때문에 내장 변수의 인덱스가 더 크다면 역순이라는 뜻
            if sorting > rule.index(towers_word):
                return '불가능'
            sorting = rule.index(towers_word)
    return '가능'    



# 입력값 
tower = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
rule = "ABD"
# 출력
print(sol(tower, rule))