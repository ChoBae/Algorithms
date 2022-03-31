# def sol(user1, user2):
#     if range(user1) > range(user2):
#         text_case = range(user2)
#     else:
#         text_case = range(user1)

#     for i in range(text_case):
#         if user1[i] == user2[i]:











# # 문자로 입력받음.
# if __name__ == '__main__':
#     user_input_1 = [i for i in input()]
#     user_input_2 = [i for i in input()]
#     print(sol(user_input_1, user_input_2))

def sol(strings):
    result = []
    for i in range(1,len(strings)+1):
        for j in range(i):
            result.append(strings[j:j+len(strings)-i+1])
            print(result)
    return result

input1 = input()
input2 = input()
#문자열 나열될 수 있는 모든 경우의수 만들기
list1 = set(sol(input1))
list2 = set(sol(input2))
#경우의 수 교집합
answers = list1.intersection(list2)
# 가장 긴 교집합
answer = max(answers,key=len)
print(len(answer))