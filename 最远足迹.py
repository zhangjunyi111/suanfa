# 开始时间18:06
#

# 最远足迹
import re


def main():
    # 接收输入字符串
    record_str = input()

    # 提取坐标
    pattern = re.compile(r'\(.*?\)')
    matchList = pattern.findall(record_str)
    # print(matchList)

    # 计算距离的平方，初始化一个最大值，和最大值的坐标
    x_max = 0
    y_max = 0
    max_distance = 0
    for coordinate in matchList:
        coordinate = list(map(int,coordinate.strip('(').strip(')').split(',')))
        # print(coordinate)
        x, y = coordinate
        distance = pow(x, 2) + pow(y, 2)
        if distance > max_distance:
            x_max = x
            y_max = y

    # 输出结果

    print(f"({x_max},{y_max})")


main()