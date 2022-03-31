# #대문자 패스

# alpha = input()

# # if alpha == alpha.upper():
# #     print('Yes')
# # else:
# #     print('No')
# ##---------------------isupper함수이용시
# if alpha.isupper():
#     print('YES')
# else:
#     print('NO')

alpha = input()

for i in alpha:
    if i.isupper():
        print(i)