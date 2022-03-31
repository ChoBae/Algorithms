# 크리스마스 별찍기

def chrismas_tree_star(n):
    for i in range(n+1):
        print(" "*(n-i)+("*"*(2*i-1)))
def main():
    y = int(input())
    chrismas_tree_star(y)
main()
