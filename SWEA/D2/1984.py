# 중간 평균값 구하기
t = int(input())
for tc in range(1, t+1):
    # 리스트 입력
    numLi = list(map(int, input().split()))
    # 최대, 최소 값 제거
    numLi.remove(max(numLi))
    numLi.remove(min(numLi))
    # 평균구해서 첫째자리 반올림
    result = round(sum(numLi) / len(numLi))
    # 출력
    print(f"#{tc} {result}")