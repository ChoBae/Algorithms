def plenet_check(num):
    plenet_li = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성']
    print(plenet_li[num-1])



def main():
    num_input = int(input())
    plenet_check(num_input)
main()