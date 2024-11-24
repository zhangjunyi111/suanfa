#
N = int(input())

# 定义一个字典，记录每个id的收入和支出
person = dict()

# id1_list , id2_list
id1_list = []
id2_list = []

# 定义支出收入

for i in range(N):
    id1, id2, money = list(input().split())
    id1_list.append(id1)
    id2_list.append(id2)
    if id2 not in person:
        person[id2] = []
    person[id2].append((id1, money))

# print('----------------')


def getMoney(money):
    return money//100 *15


def get_boss_id(id1, id2):
    for i in id2:
        if i not in id1:
            return i

        # 从boss_id开始找


boss_id = get_boss_id(id1_list, id2_list)
# boss_income = 0?

# person = {'0': [('1', '100')], '1': [('2', '100'), ('3', '200')],
#           '2': [('4', '100'), ('5', '100')], '3': [('6', '200')]}


# value [(1,300), (3,500)]
def getvalue(search_id):
    has_lower = False
    income = 0
    for key, value in person.items():
        if key == search_id:
            has_lower = True
            for lower_id, money in value:
                income += getMoney(int(money))
                money_by_lower = getvalue(lower_id)
                income += money_by_lower
            return income
    if not has_lower:
        return 0


boss_income = getvalue(boss_id)
print(boss_id,boss_income)
