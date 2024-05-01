

#
def slove_method(line):
    sum = 0
    chars = list(line)
    for i in range(len(chars)):
        c = chars[i]
        if c == '-':
            i += 1
            start = i
            while i < len(chars) and chars[i].isdigit():
                i += 1
            substring = line[start: i]
            if len(substring) > 0:
                sum -= int(substring)
            i -= 1

        if c.isdigit():
            sum += int(c)
    return sum


if __name__ == '__main__':
    lines = input()
    print(slove_method(lines))



