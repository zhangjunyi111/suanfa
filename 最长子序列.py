# 求满足条件的最长子序列
#  只能包含一个字母，其他的必须是数字

def main():
    s = input()
    # 初始化一个字母长度
    count = 0
    left = 0
    right = 0
    max_length = 0

    # 判断当前字符是数字还是字母
    # 如果是字母,判断count的大小，如果count ==1,
    # 更新最长子序列的长度
    # 那么移动右边的指针，直到为数字，然后把左指针移过来
    while right < len(s):
        char = s[right]
        if char.isalpha():
            if count == 1:
                max_length = max(max_length, right - left)
                left = postion + 1
                postion = right
                right += 1
            # 如果count的长度为0，更新count的长度，那么可以继续移动右指针
            else:
                position = right
                count += 1
                right += 1
        # 如果是数字，直接移动右指针
        elif char.isdigit():
            right += 1
    max_length = max(max_length, right - left)
    print(max_length)


if __name__ == '__main__':
    main()
