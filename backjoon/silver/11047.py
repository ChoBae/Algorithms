
# 백준 11047 '동전 0' - 그리디
# N, K int형으로 입력받기
N, K = map(int, input().split())
# 동전 리스트
coin_li = []
# 결과값 변수
result = 0 
# 입력값 N을 반복해서 동전리스트 생성
for i in range(N):
    coin_li.append(int(input()))
# 동전리스트를 reversed()를 이용해서 거꾸로 반복
for num in reversed(coin_li):
    # K가 0이면 더 이상 반복 필요 없기 때문에 break
    if K == 0:
        break
    # K가 num보다 크거나 같은 경우만
    # 동전리스트를 거꾸로 반복해주면서 //-> 몫 % -> 나머지를 활용해서 변수 처리
    if K>=num:
        result += K//num
        K = K%num
        
print(result)
