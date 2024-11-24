#  -*-  coding: utf-8  -*-
# 接收字符串
s = input()
k = int(input())
# 如何找到子串和长度, 考虑用字典
key_count = dict()
length = 0
# 遍历字符串的每个字符

# 定义个更新次数
isFirstUpdate = False


for i in range(len(s)):
    char = s[i]

    # 如果是新的字符
    if char  not  in key_count:
        key_count[char] = 1
        isFirstUpdate = True
        if i != 0:
            prev_char = s[i-1]
            key_count[prev_char] = max(key_count[prev_char],length)
            length = 0
        if i == len(s)-1:
            key_count[char] = max(key_count[char], length)

    # 如果是旧的字符
    else:
        # 旧的字符跟前面的字符相等，更新字典
        if  s[i-1] == char or length == 0 :
            if isFirstUpdate and s[i-1] == char:
                length += 1
                isFirstUpdate = False
            length += 1
            if i == len(s)-1:
                key_count[char] = max(key_count[char], length)

        else:
            prev_char = s[i - 1]
            key_count[prev_char] = max(key_count[prev_char], length)
            length = 1

res = list(key_count.values())
res.sort(reverse=True)
print(-1 if k > len(res) else res[k-1])