# ����App���࣬����App���ĸ����ԣ����ȼ�����ʼʱ�䣬����ʱ�䣬App������

class App:
    """����App�࣬���ڴ洢App�������Ϣ"""

    def __init__(self, name, priority, start_time, end_time):
        self.name = name  # App����
        self.priority = priority  # App���ȼ�
        self.start_time = start_time  # App����ʹ�õ���ʼʱ�䣨�Է���Ϊ��λ��
        self.end_time = end_time  # App����ʹ�õĽ���ʱ�䣨�Է���Ϊ��λ��

def convert_time(time_str):
    """
    ʱ��ת����������ʱ���ַ���ת��Ϊ�Է���Ϊ��λ������
    :param time_str: ʱ���ַ�������ʽΪ"Сʱ:����"
    :return: ת����ķ�����
    """
    hours, minutes = map(int, time_str.split(":"))  # ��ʱ���ַ�������":"�ָת��Ϊ����
    return hours * 60 + minutes  # ��Сʱ�ͷ���ת��Ϊ����

def main():
    n = int(input())  # ��ȡApp����
    apps = []  # ����App�б����ڴ洢����App

    for _ in range(n):
        # ѭ����ȡÿ��App����Ϣ��������App������ӵ��б���
        app_name, app_priority, app_start_time, app_end_time = input().split()
        app_priority = int(app_priority)
        app_start_time = convert_time(app_start_time)
        app_end_time = convert_time(app_end_time)
        apps.append(App(app_name, app_priority, app_start_time, app_end_time))

    query_time = convert_time(input())  # ��ȡ��ѯʱ�䣬��ת��Ϊ����
    app_at_time = "NA"  # ��ʼ����ѯʱ���Ӧ��App����Ϊ"NA"

    # ������ע��App�б�
    registered_apps = []
    for app in apps:
        if app.start_time >= app.end_time:
            continue  # �����ʼʱ�䲻С�ڽ���ʱ�䣬������

        # ������ע���App�б����ʱ���ͻ
        for i in range(len(registered_apps) - 1, -1, -1):
            registered = registered_apps[i]
            # �������ʱ���ͻ
            if max(app.start_time, registered.start_time) < min(app.end_time, registered.end_time):
                # �����ǰApp�����ȼ�������ע��App�����ȼ�
                if app.priority > registered.priority:
                    registered_apps.pop(i)  # ע�������ȼ���App
                else:
                    continue  # ������ȼ����ߣ����������һ����ע��App

        # ����ǰApp��ӵ���ע��App�б���
        registered_apps.append(app)

    # ������ע��App�б��ҵ���ѯʱ���Ӧ��App
    for app in registered_apps:
        if query_time >= app.start_time and query_time < app.end_time:
            app_at_time = app.name  # ���²�ѯʱ���Ӧ��App����
            break  # �ҵ����˳�ѭ��

    print(app_at_time)  # �����ѯʱ���Ӧ��App����

if __name__ == "__main__":
    main()
