# 이상한 369

# 내 첫풀이
# def threesixnine(user_input):
#     count = 0
#     num = 0
#     sta = False

#     while True:
#         num += 3
        

#         if num <= int(user_input):
#             for word in str(num):
#                   3의 배수-> word % 3 == 0
#                 if '3' in str(word) or '6' in str(word) or '9' in str(word):
#                     sta = True

#                 else:
#                     sta = False
#                     break   

#             if sta:
#                 count += 1
#                 print(num)
#                 sta = False

#         else:
#             break
    
#   return count
# 구글링후 다시푼것
def threesixnine(user_input):
    count = 0
    def checknum(num):
        for word in str(num):
            if int(word) == 0 or int(word) % 3 != 0:
                return 0
        return 1


           
    for num in range(0, int(user_input)+1, 3):
        count += checknum(num)

    return count
    
# 문자로 입력받음.
if __name__ == '__main__':
    user_input = str(input())
    print(threesixnine(user_input))