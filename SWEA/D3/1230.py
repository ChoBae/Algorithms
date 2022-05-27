# 암호문 3
t = 1
for tc in range(1,t+1):
    pwdLens = int(input())  # 원본 암호문의 길이
    oriPwd = list(map(str,input().split())) # 원본 암호문
    comandLens = int(input())   # 명령어의 개수
    comands = list(map(str, input().split()))    # 명령어
    comandIdx = 0
    while comandIdx != len(comands):
        # I 커맨드 (해당 인덱스에 단어 넣기)
        if comands[comandIdx] == 'I':
            x, y = int(comands[comandIdx+1]), int(comands[comandIdx+2])
            s = [] # 해당 명령어의 넣어줄 단어 리스트
            for i in range(y):
                s.append(comands[comandIdx+3+i])
            # 해당 인덱스(x)에 tmp(단어 리스트) 넣어주기
            oriPwd = oriPwd[:x] + s + oriPwd[x:]
            comandIdx += y+3
        # D 커맨드 (해당 인덱스 단어 제거)
        elif comands[comandIdx] == 'D':
            x,y = int(comands[comandIdx+1]), int(comands[comandIdx+2])
            for _ in range(y):
                oriPwd.pop(x+1)
            comandIdx += 3
        # A 커맨드 (맨뒤에 단어 추가)
        else:
            y = int(comands[comandIdx+1])
            for i in range(y):
                oriPwd.append(comands[i])
            comandIdx += y+2
    # 출력 -> 비밀번호는 10의 길이
    oriPwd = oriPwd[:10]
    print(f"#{tc} {' '.join(oriPwd)}")
