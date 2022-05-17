# 최빈수 구하기
# 입력
T = int(input())
for test_case in range(1, T + 1):
    t = int(input())
    dict = {}
    numLi = list(map(int, input().split()))
    # 숫자 리스트 -> 딕셔너리로 변환해서 중복체크
    for num in numLi:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    # 람다식으로 value(중복횟수),  key(숫자 크기) 순으로 정렬하기 -> 중복횟수가 같을때 큰 숫자를 원함 
    dict = sorted(dict.items(), key=lambda x: (x[1],x[0]) ,reverse=True)   
    # 출력
    print(f"#{t} {dict[0][0]}")