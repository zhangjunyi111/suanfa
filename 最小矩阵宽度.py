# 2 5
# 1 2 2 3 1
# 2 3 2 3 2
# 3
# 1 2 3
# start 17:00
# end

def contain_all_number(i, j, matrix, numbers_dict):
    for row in range(len(matrix)):
        for index in range(i, j + 1):
            if matrix[row][index] in numbers_dict:
                numbers_dict[matrix[row][index]] -= 1
                if numbers_dict[matrix[row][index]] == 0:
                    del numbers_dict[matrix[row][index]]
    if not numbers_dict:
        return True


def main():
    #  接收矩阵的行数和列数
    n, m = map(int, input().split())

    # 初始化矩阵matrix
    matrix = [list(map(int, input().split())) for i in range(n)]

    # 结收数字的数量
    count = int(input())



    # 接收数字
    numbers = list(map(int, input().split()))

    def get_number_dict(numbers):
        # 将数字存储到字典
        numbers_dict = {}
        for number in numbers:
            if number not in numbers_dict:
                numbers_dict[number] = 0
            numbers_dict[number] += 1
        return numbers_dict

    # 初始化最小矩阵宽度
    min_width = float('inf')
    min_left = -1
    min_right = -1
    # 逐步缩小矩阵的宽度，记录过程中min_width

    for left in range(m):
        for right in range(left, m):
            numbers_dict = get_number_dict(numbers)
            if contain_all_number(left, right, matrix, numbers_dict):
                min_width = min(min_width, right - left + 1)
                min_left = left
                min_right = right

    print(min_width, min_left, min_right)


main()
