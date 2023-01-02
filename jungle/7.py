# 1406 에디터
import sys
def main():
    def input(): return sys.stdin.readline().rstrip()
    default = list(input())
    m = int(input())
    tmp = []
    
    for _ in range(m):
        command = list(input().split())
        if command[0] == 'L':
            if default:
                tmp.append(default.pop())
                
        elif command[0] == 'D':
            if tmp:
                default.append(tmp.pop())

        elif command[0] == 'B':
            if default:
                default.pop()
                
        else:
            default.append(command[1])
            
    result = default + tmp[::-1]
    print(''.join(result))


if __name__ == '__main__':
    main()
