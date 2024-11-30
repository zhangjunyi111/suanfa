

def custom_sort(char):
    '''
    :char:待排序的字符
    :return: 该字符的ASCII
    '''
    return ord(char)

def main():
    # 接收原始字符串
    not_sorted_str=  input().strip()

    # 接收k
    k = int(input().strip())

    # 对s进行排序
    sorted_str = sorted(not_sorted_str, key=custom_sort)

    if  k>len(sorted_str):
        print(not_sorted_str.index(sorted_str[-1]))
    else:
        print(not_sorted_str.index(sorted_str[k-1]))


if __name__ == '__main__':
    main()