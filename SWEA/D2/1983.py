# 조교의 성적매기기
import math
t = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, t+1):
    # 입력
    n, k = map(int, input().split())
    stu = [0] * n
    for i in range(n):
        midterm, final, problem = map(int, input().split())
        result = (0.35 * midterm) + (0.45 * final) + (0.2 * problem)
        # 찾으려는 순서의 점수 저장
        if i == k-1:
            target = (result, i+1)
        stu[i] = (result, i+1)
    # 내림차순 정렬
    stu.sort(reverse=True)
    # grade 인덱스값 10명씩 증가할때 평점이 하나씩 증가함 EX) 30명일때 A+ 3명
    idx = math.ceil(stu.index(target) // (n//10))
    # 출력
    print(f"#{tc} {grade[idx]}")
