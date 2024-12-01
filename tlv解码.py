#
# 31
# 32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC

def get_length(hex_str):
    return int(hex_str, 16)


# 如何解码


def main():
    tag = input().strip()
    flow = input().strip().split()
    index = 0
    while index < len(flow):
        current_tag = flow[index]

        length = flow[index + 2] + flow[index + 1]
        length = get_length(length)

        if current_tag == tag:
            value = flow[index + 1 + 2:index + 1 + 2 + length]
            print(' '.join(value))
            break
        index = index + 1 + 2 + length


main()
