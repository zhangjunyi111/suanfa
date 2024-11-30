from collections import defaultdict


# 3 2
# yuwen shuxue
# fangfang 95 90
# xiaohua 88 95
# minmin 90 95
# zongfen


class Students:
    def __init__(self, name):
        '''
        :param name: 学生姓名
        '''
        # 初始化总成绩为0，各科目的成绩都为0
        self.tatal_score = 0
        self.name = name
        self.scores = defaultdict(int)

    def add_score(self, subject, score):
        '''
        :param subject: 科目
        :param score:   该科目对应的成绩
        :return:
        '''
        self.scores[subject] = int(score)
        self.tatal_score += int(score)

    def get_score(self, subject):
        '''
        :param subject: 科目
        :return: 该科目对应的成绩
        '''
        return self.scores[subject]


def main():
    # s = Students()

    # 接收学生总人数和科目总数
    n, m = map(int, input().split())

    # 接收科目
    subjects = input().split()

    # 定义一个学生列表，去存放所有的学生
    students = []

    # 接收每个学生相应科目的成绩
    for i in range(n):
        tockens = input().split()
        name = tockens[0]
        student_score = tockens[1:]
        s = Students(name)
        for j in range(m):
            s.add_score(subjects[j], student_score[j])
        students.append(s)

    rank_subject = input()

    students.sort(key=lambda s: (-s.get_score(rank_subject) if
                                 rank_subject else
                                 -s.tatal_score, s.name))

    print(' '.join([student.name for student in students]))


if __name__ == '__main__':
    main()