# 키로거
import sys
input = sys.stdin.readline
# 입력
t = int(input())

# 솔루션
for _ in range(t):
    # 유저 인풋
    userInput = input().strip()
    # 인덱싱 설정을 위한 단어의 두 부분을 나눈 리스트
    right, left= [], []
    # 인풋값 체크
    for now in userInput:
        # 위치 변경시
        # "<" 왼쪽으로 인덱스 변경(인덱스 감소)
        if now == '<':
            # left에 값이 있을 경우에 right로 옮겨줌. 
            if left:
                right.append(left.pop())
        # ">" 오른쪽으로 인덱스 변경(인덱스 증가)
        elif now == '>':
            # right에 값이 있을 경우에 left로 옮겨줌. 
            if right:
                left.append(right.pop())    
        # "-" 현재 위치의 값 제거
        elif now == '-':
            if left:
                left.pop()
        # 비밀번호 들어왔을때
        else:
            left.append(now)
    # 출력
    # 왼쪽, 오른쪽 리스트 합치기
    left.extend(reversed(right))
    print("".join(left))