# -*- coding:utf-8 -*-

import re

password = input()

lengthIsSecurity = True

# 得先进行密码处理，找到'<',并进行处理，怎么去掉<号前一位

while password.find('<') != -1:
    position = password.index('<')
    password = password.replace(password[position], '', 1)
    password = password.replace(password[position - 1], '', 1)

# 长度大于8

if len(password) < 8:
    lengthIsSecurity = False

# 匹配大写字母
reg_uppercase = re.compile(r'[A-Z]')
matches_uppercase = reg_uppercase.search(password)

# 匹配小写字母

reg_lowercase = re.compile(r'[a-z]')
matches_lowercase = reg_lowercase.search(password)

# 匹配数字

reg_number = re.compile(r'\d')
matches_number = reg_number.search(password)

# 匹配非数字字母以外的特殊字符

reg_specail = re.compile(r'\W')
matches_specail = reg_specail.search(password)

if matches_specail and matches_number and \
        matches_uppercase and matches_lowercase and lengthIsSecurity:
    print(password, 'true')

else:
    print(password, 'false')
