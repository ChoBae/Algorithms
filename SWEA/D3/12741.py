# 두 전구
# 입력
T = int(input())
answers = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    # 솔루션
    # 겹치는 거리 계산
    lens = min(b,d) - max(a,c)
    # 겹치는 거리가 음수라면 겹치지 않아서 0으로 변환시켜줌
    lens = lens if lens > 0 else 0
    answers.append(lens)

# 출력
for i in range(len(answers)):
    print(f"#{i+1} {answers[i]}")
