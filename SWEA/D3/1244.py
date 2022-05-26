# 최대 상금
# dfs
def dfs(cnt):
    global result
    # 변경 횟수를 모두 사용했을때 -> dfs 정지
    if cnt == 0:
        tmp = int(''.join(num))
        # 최대값 업데이트
        result = max(result, tmp)
        return
    # 숫자 위치 변경 과정
    for i in range(lens):
        for j in range(i+1, lens):
            num[i], num[j] = num[j], num[i]
            temp = ''.join(num)
            # 중복 체크 -> get((찾으려는 키값), 찾으려는 키값이 없을때의 값) -> 딕셔너리에 값이 없다면 1이 나오므로
            if visited.get((temp, cnt-1), 1):
                visited[(temp, cnt-1)] = 0  # 중복처리
                # dfs 진행
                dfs(cnt-1)
            num[i], num[j] = num[j], num[i]


# 입력
t = int(input())
for tc in range(1, t+1):
    num, n = input().split()
    num = list(num)  # num 리스트화 -> 인덱스 변경시 편함
    n = int(n)
    result = -10e9  # 결과값
    lens = len(num)  # 숫자판 길이
    visited = {}    # 방문 처리
    # n번의 변경 횟수만큼 dfs 진행
    dfs(n)
    # 출력
    print(f"#{tc} {result}")
