# 创建App的类，包含App的四个属性，优先级，开始时间，结束时间，App的名称

class App:
    """定义App类，用于存储App的相关信息"""

    def __init__(self, name, priority, start_time, end_time):
        self.name = name
        self.priority = priority
        self.start_time = start_time
        self.end_time = end_time


# 定义时间转换函数
def convert_time(time):
    hour, minitue = map(int, time.split(":"))
    return hour * 60 + minitue


# 定义app列表，来接收每个app

apps = []

N = int(input())

for i in range(N):
    name, priority, start_time, end_time = input().split()
    start_time = convert_time(start_time)
    end_time = convert_time(end_time)
    apps.append(App(name, priority, start_time, end_time))

query_at = convert_time(input())
query_at_app = 'NA'

registered_apps = []

for app in apps:
    if app.start_time >= app.end_time:
        continue
    for i in range(len(registered_apps) - 1, -1, -1):
        registered_app = registered_apps[i]
        if max(app.start_time, registered_app.start_time) < min(app.end_time,
                                                                registered_app.end_time):
            if app.priority > registered_app.priority:
                registered_apps.pop(i)

            else:
                continue
    registered_apps.append(app)

for app in registered_apps:
    if app.start_time <= query_at and app.end_time > query_at:
        query_at_app = app.name

print(query_at_app)












