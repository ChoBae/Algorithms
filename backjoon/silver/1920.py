# 수찾기 실버4 이분탐색
# 입력
n = int(input())
nLi = list(map(int, input().split()))
m = int(input())
mLi = list(map(int, input().split()))
# 이분탐색을 위한 정렬
nLi.sort()
#  이분 탐색 과정
def binary(num):
    # 시작, 끝값 설정
    start= 0; 
    end= len(nLi)-1; 
    # 탐색까지 반복
    while end-start>= 0:
        mid = (start+end)//2
        if nLi[mid] == num:
            return True
        else:
            # 중간값보다 크면 시작값을 중간에 오른쪽 수(큰수)로 바꿈
            if nLi[mid] < num:
                start = mid+1
            # 중간값보다 작으면 끝값을 중간값의 왼쪽 수(작은수)로 바꿈 
            else:
                end = mid-1
    return False
# 출력
for numM in mLi:
    if binary(numM):
        print(1)
    else:
        print(0)