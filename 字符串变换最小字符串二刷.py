# 字符串变换最小字符串二刷
# bcaacd
# acabcd
import sys


def main():
    s = input().strip()
    # 将s转化为列表
    str_list = list(s)
    new_str_list = sorted(str_list)
    # 要考虑相等的情况，相等的话，直接输出即可
    if str_list == new_str_list:
        print(s)
        sys.exit()

    for i in range(len(str_list)):
        if new_str_list[i] != str_list[i]:
            # replace_index = str_list.index(new_str_list[i])
            replace_index = -1
            # 要从 i+1开始遍历，要统计最后出现的位置，进行交换
            for j in range(i + 1, len(str_list)):
                if str_list[j] == new_str_list[i]:
                    replace_index = j
            str_list[i], str_list[replace_index] = str_list[replace_index], \
                                                       str_list[i]
            print(''.join(str_list))
            break

if __name__ == '__main__':
    main()