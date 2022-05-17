# 백만 장자 프로젝트
# 입력
# T = int(input())
# for test_case in range(1, T + 1):
#     num = int(input())
#     salePrices = list(map(int,input().split()))
#     nowPrice = []
#     result = 0
#     for salePrice in salePrices:
#         # 비었을거나 최근에 구매가보다 작거나 같으면 일단 구매.
#         if not nowPrice or nowPrice[-1] <= salePrice:
#             nowPrice.append(salePrice)
#         # 다음 구매가가 마지막 산 구매가보다 작을때 지금까지 산것 다팔고 이득보기
#         elif nowPrice[-1] > salePrice:
#             # 마지막에 넣었던 가격으로 판매
#             for now in nowPrice[:-1]:
#                 result += nowPrice[-1] - now
#             # 현재 구매가로 초기화
#             nowPrice = [salePrice]
#     # 남은 거래 진행
#     for now in nowPrice[:-1]:
#         result += nowPrice[-1] - now
#     # 출력
#     print(f"#{test_case} {result}")

# 입력
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    salePrices = list(map(int, input().split()))
    nowPrice = -10e9
    result = 0
    # 구매가 상황을 거꾸로 진행
    for salePrice in reversed(salePrices):
        # 초기값, 현재 판매할수있는 최고가 업데이트
        if nowPrice < salePrice:
            nowPrice = salePrice
        # 현재 최고가에 판매-> 이득보기
        else:
            result += nowPrice - salePrice
    # 출력
    print(f"#{test_case} {result}")
