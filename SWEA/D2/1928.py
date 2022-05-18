# Base64 Decoder 
# 입력
# 라이브러리 사용 풀이
# from base64 import b64decode

# T= int(input())
# # 솔루션
# for test_case in range(1, T + 1):
#     word = input()
#     res = b64decode(word).decode('UTF-8')
#     print(f"#{test_case} {res}")
    
    
    
# 라이브러리 사용 X 풀이
# base64 encoding 값
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/'
      ]
T= int(input())
# 솔루션
for tc in range(1, T + 1):
    word = input()
    tmp = ''
    for i in range(len(word)):
        num = decode.index(word[i])
        # 이진수 변환시 '0b'가 붙기때문에 제거
        bin_num = str(bin(num)[2:])
        # 6비트까지 앞에 0을 붙혀줌 0 -> 000001
        while len(bin_num) < 6:
            bin_num = '0' + bin_num
        tmp += bin_num
    result = '' # 출력 값
    # 출력값 구하기
    for j in range(len(word)* 6 // 8):
        # 8비트씩 잘라서 10진수화
        sentence = int(tmp[j*8 : j*8 + 8], 2)
        result += chr(sentence)
    # 출력
    print(f"#{tc} {result}")