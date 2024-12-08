# 考察递归

# 分月饼

# 思路
# 按照月饼的数量进行排序，第n-1个比第n个最多多3个
distribute_method = []


def distribute(num, have_distributed, method, m, n):
    global distribute_method
    if have_distributed == m:
        # 提前去重，不添加到结果列表
        # 排序的时候，不能动method，因为method还要进行回溯
        method_new = sorted(method)
        if method_new  in distribute_method:
            return
        distribute_method.append(method_new.copy())
        return

    for i in range(1, num):
        have_distributed += 1
        method.append(i)
        if have_distributed == m:
            method.pop()
            method.append(n - sum(method))
        distribute(num - i, have_distributed, method, m, n)
        have_distributed -= 1
        method.pop()


def main():
    m, n = map(int, input().split())
    have_distributed = 0
    method = []
    # 列出所有的分配方案
    # 尝试从n个月饼中分配1-n个
    distribute(n, have_distributed, method, m, n)
    print(distribute_method)
    # 排除不符合要求的


main()
