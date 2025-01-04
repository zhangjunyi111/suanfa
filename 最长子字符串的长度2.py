def find_longest_substring_length(s):
    n = len(s)
    max_length = 0
    for i in range(n):
        l_count = 0
        x_count = 0
        o_count = 0
        for j in range(n):
            index = (i + j) % n
            ch = s[index]
            if ch == 'l':
                l_count += 1
            elif ch == 'x':
                x_count += 1
            elif ch == 'o':
                o_count += 1

            if l_count % 2 == 0 and o_count % 2 == 0 and x_count % 2 == 0:
                max_length = max(max_length, j + 1)
    # return的位置缩进要和for对齐
    return max_length


if __name__ == "__main__":
    s = input()
    max_length = find_longest_substring_length(s)
    print(max_length)
