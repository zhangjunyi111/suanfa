# start time:18:28
# end time
# 寻找符和要求的最长子串

from collections import defaultdict


def main():
    # 初始化一个char_index_dict
    char_index_dict = defaultdict(list)

    # 存储要排除的字符
    exclude_char = input()

    # 存储字符串s
    s = input()

    # 初始化一个左右指针，用于生成滑动窗口
    left = 0
    right = 0

    # 初始化一个最长符合要求的字符串长度
    max_length = 0

    # 设置遍历的边界，当右指针移动到字符串最右边的时候，结束遍历，输出max_length
    while right < len(s):
        # 记录当前的字符s
        current_char = s[right]

        # 如果当前的s等于被排除的字符，将左右指针，全部移动到当前位置的下一个位置
        if current_char == exclude_char:
            # 更新最长字符串的位置
            max_length = max(max_length, right - left)
            right += 1
            left = right

        else:
            # 如果当前字符在滑动窗口中的数量超过2，那么移动左指针，将左指针的位置移动到该字符在窗口中第一次出现的位置的下一个位置
            # 然后将当前字符的位置加入到字典中
            # 更新右指针的位置

            if current_char not in char_index_dict.keys():
                char_index_dict[current_char]

            char_index = char_index_dict[current_char]
            if len(char_index) == 2:
                # 更新最长字符串的长度
                max_length = max(max_length, right - left)
                left = char_index[0] + 1
                char_index.pop(0)
                char_index.append(right)
                right += 1

            else:
                char_index.append(right)
                right += 1
    max_length = max(max_length,right-left)
    print(max_length)


if __name__ == '__main__':
    main()
