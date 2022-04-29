# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline
n, m = map(int , input().split())
# 포켓몬 이름, 인덱스 딕셔너리 (각각 구성)
poketmonIdx = {}
poketmonName = {}

# 솔루션
# 포켓몬 입력
for i in range(n):
    tmp = input().strip()
    # 딕셔너리에 각각 인덱스 맞춰서 추가하기
    poketmonIdx[i+1] = tmp
    poketmonName[tmp] = i+1
# 문제 풀이
for _ in range(m):
    tmp = input().strip()
    # 문자가 들어왔을때
    if tmp.isalpha():
        print(poketmonName[tmp])
    # 숫자가 들어왔을때
    else:
        print(poketmonIdx[int(tmp)])
