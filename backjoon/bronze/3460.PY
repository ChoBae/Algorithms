#3460 이진수
def solve(T):
    
    for i in range(T):
        bin = []
        num = 0
        result =[]
        n = int(input())
        while True:

            if n ==0:
                break
            else:
                bin.append(n%2)
                n = int(n /2)
    
        for i in bin:
            if int(i) == 1:
                result.append(num)
                num +=1
            else:
                num +=1
        
        print(str(result))


def main():
    #1. 입력
    T = int(input())
    solve(T)


main()
