# 交换A组芯片和B组芯片，使得A和B的芯片总算力接近
#  a +y -x = b+x -y
# x -y = (a-b)//2
# x - (a-b)//2 =y


def main():
    n, m = map(int, input().split())

    # 计算A组芯片的总算力和B组芯片的总算力

    chips_A = list(map(int, input().split()))
    chips_B = list(map(int, input().split()))
    chips_A.sort()
    chips_B.sort()

    sum_chips_A = sum(chips_A)
    sum_chips_B = sum(chips_B)

    # 计算chips_A 与chips_B的差值的1/2
    # 四舍五入取整数
    diff = round((sum_chips_A - sum_chips_B) /2)

    for x in chips_A:
        if x-diff  in chips_B:
            print(x,x-diff)
            break


main()

