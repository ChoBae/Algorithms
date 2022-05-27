# 암호문 1
t = 10
for tc in range(1, t+1):
    pwdLens = int(input())  # 원본 암호문의 길이
    oriPwd = list(map(str,input().split())) # 원본 암호문
    comandLens = int(input())   # 명령어의 개수
    comands = list(map(str, input().split('I')))    # 명령어
    # I로 split() 해주어서 맨앞에 공백이 나와서 제거
    comands = comands[1:]
    # 명령어 만큼 반복
    for comand in comands:
        comand = comand.split()
        x, y= int(comand[0]), int(comand[1])
        tmp = [] # 해당 명령어의 넣어줄 단어 리스트
        for i in range(y):
            tmp.append(comand[2+i])
        # 해당 인덱스(x)에 tmp(단어 리스트) 넣어주기
        oriPwd = oriPwd[:x] + tmp + oriPwd[x:]
    # 출력 -> 비밀번호는 10의 길이
    oriPwd = oriPwd[:10]
    print(f"#{tc} {' '.join(oriPwd)}")
