# 진법변환 브론즈2
# 파이썬 int함수 풀이 int(n진법의 수 b, n진법) -> 10진법 변환
# b, n = input().split()
# print(int(b, int(n)))


# 함수 사용 x 풀이

b, n = input().split()
b = b[::-1] # n진법의 수 b를 거꾸로 전환
n = int(n)
idx = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 각 해당하는 10진수 인덱스
answer = 0 # 결과값
for i in range(len(b)):
    # 해당하는 인덱스값 * n진법의 제곱
    answer += idx.index(b[i]) * (n ** i)
# 결과 출력
print(answer)
