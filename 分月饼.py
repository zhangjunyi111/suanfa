

# 考察递归

# 分月饼

# 思路
# 按照月饼的数量进行排序，第n-1个比第n个最多多3个
distribute_method = []
def distribute(num,have_distributed,method,m):
    global  distribute_method
    if have_distributed == m:
        distribute_method.append(method)
        return

    for i in range(1,num):
        method.append(i)
        have_distributed += 1
        distribute(num - i, have_distributed, method,m)
        have_distributed -= 1
        method.pop()

def main():
    m,n = map(int,input().split())
    have_distributed = 0
    method =[]
    # 列出所有的分配方案
    # 尝试从n个月饼中分配1-n个
    distribute(n,have_distributed,method,m)


    # 排除不符合要求的

main()