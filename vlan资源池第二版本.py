# 修改不合理的名称


# 将输入中的那些范围转化为单个

def get_vlan_pools(vlan_group):
    # 遍历vlan_pool池子，如果是带-格式的按照一种方法处理，如果是单独的一个，按照一种方式处理
    vlan_pool = []
    for vlan_item in vlan_group:
        if vlan_item.__contains__('-'):
            start, end = map(int, vlan_item.split('-'))
            for i in range(start, end+1):
                vlan_pool.append(i)
            continue
        else:
            vlan_pool.append(int(vlan_item))

        return vlan_pool


# 移除功能实现
def remove(orignal_vlan, be_remove_vlan):
    for element in be_remove_vlan:
        if element in orignal_vlan:
            orignal_vlan.remove(element)
    return orignal_vlan


def megre_element(res):
    '''
    优化后直接输出要求的结果
    :param res:
    :return:
    '''
    megre_result = []
    vlan_element = []
    vlan_element.append(res[0])
    i = 0
    while i < (len(res)-1):
        if res[i]+1 == res[i+1]:
            vlan_element.append(res[i+1])
            i += 1
        else:
            megre_result.append(vlan_element)
            vlan_element = []
            vlan_element.append(res[i+1])
            i += 1
    if vlan_element:
        megre_result.append(vlan_element)

    res = []
    for vlan in megre_result:
        if len(vlan) == 1:
            res.append(str(vlan[0]))
        else:
            start, end = vlan[0], vlan[-1]
            res.append(str(start) + "-" + str(end))
    return ','.join(res)


if __name__ == '__main__':
    orignal_vlan = get_vlan_pools(input().split(','))
    be_removed_vlan = get_vlan_pools(input().split(','))
    res = remove(orignal_vlan, be_removed_vlan)
    res.sort()
    res = megre_element(res)
    print(res)










