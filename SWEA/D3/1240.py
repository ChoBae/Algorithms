# 단순 2진 암호코드
t= int(input())
# 1~9 넘버링
numbering = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
for tc in range(1, t+1):
    # 입력
    n, m = map(int, input().split())
    pwds = [input() for _ in range(n)]  # 암호 패스워드 리스트 
    check = False # 암호가 맞는지 체크 boolean
    # 암호 패스워드 리스트 반복
    for pwd in pwds:
        # 암호 패스워드에 1이 들어있다면 체크.
        if '1' in pwd:
            # 암호 패스워드가 시작점이 애매해서 뒤에서 시작점을 찾는다.
            text = ''  
            t = False
            for i in range(m-1,0,-1):
                # 패스워드 길이를 다채웠을때 break (7 * 8)
                if len(text) == 56:
                    break
                # 뒤에서 부터 검사하다가 1일때 True 처리해서 값을 넣어주기 시작함
                if pwd[i] == '1':
                    t = True
                if t:
                    text += pwd[i]
            # 거꾸로 구했기때문에 돌려주기
            text = text[::-1]
            # 각 7자리의 암호에 맞는 숫자 찾아 answer에 넣어주기
            answer = ''
            for i in range(0,56,7):
                if text[i:i+7] in numbering:
                    answer += str(numbering.index(text[i:i+7]))
                else:
                    break
            # 8개의 암호가 아니라면 다음 암호 패스워드로 가기
            if len(answer) !=8:
                continue
            # 8개의 암호일때 검사시작
            result, odd = 0 , 0
            # 암호의 조건 -> 홀수번째 더해서 * 3 + 짝수번째 더하기
            for i in range(1,8):
                if i % 2 == 0:
                    result += int(answer[i-1])
                else:
                    odd += int(answer[i-1])
            # 홀수번째 연산값과 마지막 검증코드 더해주기
            result += odd * 3 + int(answer[-1])
            # 암호코드가 10의 배수라면 정상코드
            if result % 10 == 0:
                # 검증코드의 합 구하기
                res = 0
                for i in answer:
                    res += int(i)
                check = True # 암호코드가 정상처리
                break
    # 출력
    print(f"#{tc}", end=' ')
    # 암호코드가 정상일때 검증코드의 합 출력
    if check:
        print(res)
    # 암호코드가 비정상일때 0
    else:
        print(0)
                