# 8595 히든 넘버
def main():
    n = int(input())
    word = input()
    hiddenNum = ''
    for i in range(n):
        if word[i].isdigit():
            hiddenNum += word[i]
        else:
            hiddenNum += ' '
                
    print(sum(list((map(int, hiddenNum.split())))))
        
if __name__ == '__main__':
    main()
    
