# 最短木板长度
# 开始时间：16:45
# 结束时间：17:23

# 解题思路：引入堆排序
import heapq


def main():
    # 接收木板的个数列表和木料的长度m
    n, m = map(int, input().split())
    # 接收木板的长度列表
    woodlist = list(map(int, input().split()))
    # 对木板的长度列表进行排序
    heapq.heapify(woodlist)
    # 当木板的长度不为0时，对最短的木板补齐1m,然后重新排序
    while m > 0:
        #  弹出木板的长度列表的最小值
        minwood = heapq.heappop(woodlist)
        # 木料的长度减少1m
        m -= 1
        # 最短木板的长度增加1m
        newwood = minwood + 1
        # 将新木板的长度放入木板的列表中
        heapq.heappush(woodlist, newwood)

    res = heapq.heappop(woodlist)
    print(res)


if __name__ == "__main__":
    main()
