

# 将输入中的那些范围转化为单个

def convert_vlan(s):
    for element in s:
        start, end = map(int, element.split('-'))
        res = []
        for i in range(start, end+1):
            res.append(i)
        return res


# 移除功能实现
def remove(orignal_vlan, be_remove_vlan):
    for element in be_remove_vlan:
        if element in orignal_vlan:
            orignal_vlan.remove(element)
    return orignal_vlan


def megre_element(res):
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
    return megre_result


def repalce_element(vlans):
    vlan_new = []
    for i in range(len(vlans)):
        if vlans[i].__contains__('-'):
            # orignal_vlan[i] = convert_vlan(orignal_vlan[i])
            vlan_new.extend(convert_vlan(vlans))
        else:
            vlan_new.append(int(vlans[i]))
            del vlans[i]

    return vlan_new


if __name__ == '__main__':
    orignal_vlan = input().split(',')
    be_removed_vlan = input().split(',')
    orignal_vlan = repalce_element(orignal_vlan)
    be_removed_vlan = repalce_element(be_removed_vlan)
    res = remove(orignal_vlan, be_removed_vlan)
    res.sort()
    res = megre_element(res)
    res_ = []
    for vlan in res:
        if len(vlan) == 1:
            res_.append(str(vlan[0]))
        else:
            start, end = vlan[0], vlan[-1]
            res_.append(str(start) + "-" + str(end))
    print(','.join(res_))









