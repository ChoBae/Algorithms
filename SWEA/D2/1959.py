# 두개의 숫자열
t = int(input())
for tc in range(1, t+1):
    # 입력
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # n개의 수열
    b = list(map(int, input().split()))  # m개의 수열
    result = 0  # 결과값
    # 시작점 구하기 (길이가 짧은 수열 설정)
    for i in range(n-m+1 if len(a) > len(b) else m-n+1):
        tmp = 0 # 현재 시작점의 결과값
        # 짧은 수열의 길이만큼 반복
        for j in range(m if len(a) > len(b) else n):
            tmp += a[i+j] * b[j] if len(a) > len(b) else b[i+j] * a[j]
        # 최대값 업데이트
        result = max(result, tmp)
    # 출력
    print(f"#{tc} {result}")
