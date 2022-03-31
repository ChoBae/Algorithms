# 10진수-> 2진수 13-> 1101 8, 4, 0 , 1   0b111000011011101
user_input = int(input())
bin = []
#이부분 수정.
for i in range(user_input, -1 ,-1):
  
    if 2**i <= user_input:
        user_input = user_input-(2**i)
        
        bin.append('1')
    
    else:
        bin.append('0')
print(bin)
