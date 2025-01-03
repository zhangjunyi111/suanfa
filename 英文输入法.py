# 英文输入法
import string


def main():
    # 接收用户输入
    sentence = input()

    # 接收prefix
    prefix = input()

    # 对sentence进行简单的处理
    # translate前面的对象是要转换的字符串
    sentence = sentence.translate(str.maketrans(string.punctuation, ' ' * len(
        string.punctuation)))

    # 构建字符集，用set构建
    wordset = set(sentence.split())

    # 初始化答案列表
    ans = []

    for s in wordset:
        if s.startswith(prefix):
            ans.append(s)
            ans.sort()
    if ans:
        print(' '.join(ans))
    else:
        print(prefix)


if __name__  == '__main__':
    main()