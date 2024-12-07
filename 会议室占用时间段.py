import re


def main():
    # 输入的格式要注意，要对输入字符字符进行处理，转化为需要的列表形式
    arr = input()
    arr = list(map(int,re.sub(r"[\[\]]",'',arr).split(',')))
    new_arr = []
    for i in range(0,len(arr),2):
        new_arr.append([arr[i],arr[i+1]])

    new_arr.sort(key=lambda x: x[0])
    current_item = new_arr[0]
    res = []
    res.append(current_item)
    for next_item in new_arr[1:]:
        if current_item[1] > next_item[0]:
            current_item[1] = max(current_item[1], next_item[1])

        elif current_item[1] < next_item[0]:
            res.append(next_item)
            current_item = next_item

        elif current_item[1] == next_item[0]:
            current_item[1] = next_item[1]
    # 输出格式要注意
    # print(res)
    print('[',end='')
    for i ,time in enumerate(res):
        print(f"[{time[0]},{time[1]}]",end='')
        if i < len(res) -1:
            print(',',end='')
    print(']')
main()