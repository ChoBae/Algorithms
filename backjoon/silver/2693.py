# 3번째로 큰 수 찾기
# TEST CASE
T = int(input())
# 결과값
resultList = []
# 
for i in range(T):
    # 리스트값으로 받아서 정렬후 결과값 리스트으로 append
    nums = list(map(int,input().split()))
    nums.sort()
    resultList.append(nums)

# 오름차순으로 정렬됐기때문에 뒤에서 3번째수 출력
for nums in resultList:
    print(nums[-3])
    