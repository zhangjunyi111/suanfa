import math


def main():
    # 接收芯片容量
    # 接收芯片数量
    # 接收用户的配置序列
    m = int(input())
    n = int(input())
    user_config_sequence = input()
    board_card = [1.25 * m] * n

    # 建立用户配置字典
    config = dict()
    config["A"] = 1.25 * 1
    config["B"] = 1.25 * 2
    config["C"] = 1.25 * 8

    for option in user_config_sequence:
        need = config[option]
        for j in range(n):
            if board_card[j] >= need:
                board_card[j] -= need
                break

    for i in range(n):
        unused = math.floor(board_card[i]/1.25)
        used = m - unused
        print(used*'1' + unused*'0')



main()