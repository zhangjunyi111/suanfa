import sys

# ��ȡ��������N
numberOfRows = int(input())
# ��ȡÿ��������Ҫ��Ԫ������K
numberOfColumns = int(input())

# ���������б����ڴ洢ÿ���б��Ԫ��
queueList = []
while True:
    try:
        queueList.append(list(map(int, input().split())))
    except:
        break

# ����һ���б����ڴ洢���յ�Ԫ������
matrix = [0] * (numberOfColumns * numberOfRows)
matrixIndex = 0  # ���ڱ�ǵ�ǰ��䵽matrix�б��е�λ��
queueIndex = 0  # ���ڱ�ǵ�ǰ����Ķ�������

# ѭ����ֱ��matrix�б���ȫ����
while matrixIndex < len(matrix):
    didRemoveQueue = False  # ��Ǳ���ѭ�����Ƿ��ж��б��Ƴ�

    # ����ÿ�����ڣ������Դӵ�ǰ������Ϊÿ��������ȡһ��Ԫ��
    for i in range(numberOfRows):
        if not queueList:  # ������ж��ж��Ѵ�����ϣ����˳�ѭ��
            break
        # �����ǰ����Ϊ�գ����Ƴ��ö���
        if not queueList[queueIndex]:
            queueList.pop(queueIndex)
            if not queueList:
                break
            queueIndex %= len(queueList)
            didRemoveQueue = True
        # �����ǰ���в�Ϊ�գ���Ӷ�����ȡ��һ��Ԫ����䵽matrix�б���
        if queueList and queueList[queueIndex]:
            matrix[matrixIndex] = queueList[queueIndex].pop(0)
            matrixIndex += 1
            if matrixIndex >= len(matrix):
                break

    # �������ѭ��û�ж��б��Ƴ������Ҷ����б�Ϊ�գ�������һ������
    if not didRemoveQueue and queueList:
        queueIndex = (queueIndex + 1) % len(queueList)

# ���մ���˳�򹹽�����ַ���
for row in range(numberOfRows):
    for col in range(numberOfColumns):
        print(matrix[col * numberOfRows + row], end=" ")


