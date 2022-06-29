# 넘버 게임
def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

t = int(input())
for _ in range(t):
    n = input()
    for i in range(2, 7):
        print(solution(int(n), i))