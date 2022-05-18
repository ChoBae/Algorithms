# 패턴마디의 길이
T= int(input())
# 솔루션
for tc in range(1, T + 1):
    sts = input()
    pattern = ''
    # 패턴찾기
    for i in range(len(sts)):
        # 초기값이거나, 현재까지 저장된 패턴의 값 패턴이 아니면 패턴에 값추가
        if len(pattern) == 0 or sts[i:i+i] != pattern:
            pattern += sts[i]
        # 현재까지 저장된 패턴이 이후 패턴으로 나오면 break
        elif sts[i:i+i] == pattern:
            break
    # 출력
    result = len(pattern)
    print(f"#{tc} {result}")
            