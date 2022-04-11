# 나이순 정렬 실버 5
n = int(input())    # 테스트 케이스 수
memberList = [] # 멤버 리스트
# 솔루션
for i in range(n):
    age, name= map(str,input().split()) # 나이, 이름 
    memberList.append((i, int(age), name))  # 인덱싱처리해서 넣어주기
# 람다식으로 정렬
memberList.sort(key=lambda x:(x[1],x[0]))
# 출력
for member in memberList:
    mAge = member[1]
    mName = member[2]
    print(mAge, mName)