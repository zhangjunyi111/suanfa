#  -*-  coding: utf-8  -*-
import re

s = input()
#  5*6-3+2abcd0-1+2-3+4-5+6-7+8-9
# 从s中拿到所有的表达式，放到列表中
start = -1
operator = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operand = ['+', '-', '*', '/']

expression = []

i = 0
flag= False
while i < len(s):
    # 如果当前字符是操作数的话，将索引的值给到start,并将i的值+1，并遍历后续的字符，如果后续的字符满足条件，就加1否则就退出循环
    if s[i] in operator:
        if not flag:
            start = i
            flag = False
        i += 1
        if  i< len(s) and  s[i] in operator:
            flag = True
            continue
        while (s[i] in operand and (s[i - 1] in operator if i != 0 else True
        )) or (s[i] in operator and (s[i - 1] in operand if i != 0 else
        True)) or (s[i] in operator and (s[i - 1] in operator if i != 0 else
        True)) :
            i += 1
            if len(s) <= i:
                break
    if start != -1:
        tmp = s[start: i]
        expression.append(tmp)
        start = -1
    i += 1

# print(expression)
# 排序比较长度
expression = sorted(expression, key=lambda x: len(x))

# 使用正则分割表达式，计算值

max_expression = ''

for express in expression:
    if len(express) > len(max_expression):
        max_expression = express

tokens = re.split(r'([-+*])', max_expression)
# tokens = re.split('([-+*])', expression)

tockens = [token for token in tokens if token]

while '*' in tockens:
    position = tockens.index('*')
    res = int(tockens[position - 1]) * int(tockens[position + 1])
    tockens = tockens[:position - 1] + [str(res)] + tockens[position + 2:]

result = int(tockens[0])
for i in range(1,len(tockens),2):
    if tockens[i] == '+':
        result += int(tockens[i+1])
    else:
        result -= int(tockens[i+1])

print(result)


