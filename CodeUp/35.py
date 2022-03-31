def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two

num1 = one(2)
num2 = one(3)
num3 = one(4)
print(num1(10))
print(num2(10))
print(num3(10))