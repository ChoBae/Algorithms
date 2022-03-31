nums = list(map(int, input().split()))

if nums != sorted(nums):
    print('No')
else:
    print('Yes')