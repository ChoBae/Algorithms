


N = int(input())
km = list(map(int, input().split()))
pay = list(map(int, input().split()))
result = 0
pay_set = sorted(pay[:-1])


while True:
    
    if pay[0] != pay_set[0]:
        result += pay[0] * km[0]
        pay.pop(0)
        km.pop(0)
    else:
        result += pay[0] * sum(km)
        break

print(result)

