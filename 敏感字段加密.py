
# 接收索引
k = int(input())

# 接收命令字符串并转化为列表
s = list(input())

# 生成所有的命令字算法
commad_word = ''
commad_word_list = []

i = 1
for word in s:
    if word == '_':
        if commad_word.__contains__('"'):
            commad_word += word
        else:
            if commad_word:
                commad_word_list.append(commad_word)
            commad_word = ''
    elif len(s) == i:
        commad_word += word
        commad_word_list.append(commad_word)
        commad_word = ''

    elif word == '"':
        if commad_word.__contains__('"'):
            commad_word += word
            commad_word_list.append(commad_word)
            commad_word = ''
        else:
            commad_word += word

    else:
        commad_word += word
    i += 1

print(commad_word_list)
if len(commad_word_list)-1 < k:
    print('ERROR')
else:
    commad_word_list[k] = '******'

print('_'.join(commad_word_list))


# password__a12345678_timeout_100




