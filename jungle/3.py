# 백준 11816
# 8진수, 10진수, 16진수 입력받아 10진수로 출력하기

def main():
    x = str(input())
    # 10진수 일 경우 0으로 시작하지 않음
    if x[0] != '0':
        print(int(x))
        return
    # 8진수 일 경우 0o로 시작 -> 8진수로 변환, 16진수 일 경우 0x로 시작 -> 16진수로 변환
    print(int(x, 8) if x[1] != 'x' else int(x, 16))
if __name__ == '__main__':
    main()
    