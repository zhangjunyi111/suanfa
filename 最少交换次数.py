# 接收数组
# 接受阈值
# 整体思路就是二值化后，统计每个窗口中1的个数，找出出现1的个数最大的，然后用窗口大小减去它，就是需要交换的次数最小

def main():
    arr = list(map(int, input().strip().split()))
    thord = int(input())
    window_size = sum([1 for x in arr if x < thord])
    arr_new = []
    # 将arr数组二值化
    for x in arr:
        if x < thord:
            arr_new.append(1)
        else:
            arr_new.append(0)
    maxinwindow = 0
    for i in range(0, len(arr)):
        if i + window_size > len(arr):
            maxinwindow = max(maxinwindow, arr_new[i:len(arr)].count(1))
        # print(i,arr[i:i + window_size],arr_new[i:i + window_size].count(1))
        maxinwindow = max(maxinwindow, arr_new[i:i + window_size].count(1))

    print(maxinwindow)
    print(window_size)
    print(window_size-maxinwindow)


main()