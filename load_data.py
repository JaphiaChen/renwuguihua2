import os
rootdir = os.path.dirname(__file__)


# 导入数据
def load_data():
    '''
    读取数据点信息
    :return: 数据点构成的列表
    '''
    points = []
    with open(os.path.join(rootdir, "test_points.txt"))as inputFile:
        num = int(inputFile.readline().strip())
        for _ in range(num):
            items = inputFile.readline().strip().split(',')
            items[1:4] = map(float, items[1:4])
            points.append(items)
    return points
