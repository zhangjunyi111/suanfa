# 字符串变换最小字符串二刷
# abdc
# abcd

def main():
    s = input().strip()
    # 将s转化为列表
    str_list = list(s)
    new_str_list = sorted(str_list)

    for i in range(len(str_list)):
        if new_str_list[i] != str_list[i]:
            replace_index = str_list.index(new_str_list[i])
            str_list[i], new_str_list[replace_index] = str_list[replace_index], \
                                                        new_str_list[i]
            print(''.join(str_list))
            break
