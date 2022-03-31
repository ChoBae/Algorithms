result = ""
while True:
    a = input()
    if a == 'q':
        result += a
        for i in result:
            print(i)
        break
    else:
        result += a