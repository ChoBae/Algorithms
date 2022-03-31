# 버블정렬

def bubble(n, data):
    # 수의 처음부터 끝전까지 비교.
    for i in range(n-1):
        # 버블정렬은 1회차마다 마지막 수가 가장큰 수 -> 그래서 범위를 하나씩 줄여줌 
        for j in range(n-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    for i in range(n):
        print(data[i], end=" ")

n = int(input())
data = list(map(int, input().split()))

bubble(n, data)