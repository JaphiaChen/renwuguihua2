import os
import numpy as np
import math as m
import random
import matplotlib.pyplot as plt
import evaluate as eva

# flame.txt
# Jain_cluster=2.txt
# Aggregation_cluster=7.txt
# Spiral_cluster=3.txt
# Pathbased_cluster=3.txt

rootdir = os.path.dirname(__file__)

# 导入数据
def load_data():
    points = []
    with open(os.path.join(rootdir, "test_points.txt"))as inputFile:
        num = int(inputFile.readline().strip())
        for _ in range(num):
            items = inputFile.readline().strip().split(',')
            items[1:4] = map(float, items[1:4])
            points.append(items)
    return points


def cal_dis(data, clu, k):
    """
    计算质点与数据点的距离
    :param data: 样本点
    :param clu:  质点集合
    :param k: 类别个数
    :return: 质心与样本点距离矩阵
    """
    dis = []
    for i in range(len(data)):
        dis.append([])  # 有多少个点就有多少个子矩阵
        for j in range(k):  # 每个子矩阵里有k个元素，分别对于该点到各质心的距离
            dis[i].append(m.sqrt((data[i][1] - clu[j, 0])**2 + (data[i][2]-clu[j, 1])**2))
    return np.asarray(dis)


def divide(data, dis):
    """
    对数据点分组
    :param data: 样本集合
    :param dis: 质心与所有样本的距离
    :return: 分割后样本
    """
    clusterRes = [0] * len(data)    # 初始化分类均为0
    for i in range(len(data)):  # 逐点遍历
        seq = np.argsort(dis[i])    # 到各质心的距离从小到大排序，输出index
        clusterRes[i] = seq[0]  # 把该点分给最小距离那一类
    return np.asarray(clusterRes)


def center(data, clusterRes, k):
    """
    计算质心
    :param group: 分组后样本
    :param k: 类别个数
    :return: 计算得到的质心和各类的点数
    """
    clunew = []
    k_sum = []
    for i in range(k):
        x_sum = 0
        y_sum = 0
        k_sum.append(0)
        # 计算每个组的新质心
        for j in range(len(data)):
            if clusterRes[j] == i:
                x_sum = x_sum+data[j][1]    # 按列相加，即x、y轴的分别和
                y_sum = y_sum+data[j][2]
                k_sum[i] = k_sum[i] +1
        avg_sum = x_sum/k_sum[i], y_sum/k_sum[i]
        clunew.append(avg_sum)  # 添加该类点的新质心
    clunew = np.asarray(clunew)
    return clunew


def classfy(data, clu, k):
    """
    迭代收敛更新质心
    :param data: 样本集合
    :param clu: 质心集合
    :param k: 类别个数
    :return: 误差， 新质心
    """
    clulist = cal_dis(data, clu, k)
    clusterRes = divide(data, clulist)
    clunew= center(data, clusterRes, k)
    err = clunew - clu
    return err, clunew, k, clusterRes


def plotRes(data, clusterRes, clunew, clusterNum):
    """
    结果可视化
    :param data:样本集
    :param clusterRes:聚类结果
    :param clusterNum: 类个数
    :return:
    """
    nPoints = len(data)

    # 输出分类结果
    Target_types = []
    type_num =[]
    outputFile = open('cluster_result.txt', mode='a+')
    for i in range(clusterNum):
        type_num.append(0)
        Target_types.append([])
        for j in range(nPoints):
            if clusterRes[j] == i:
                Target_types[i].append(data[j])
                type_num[i] =type_num[i] + 1
        outputFile.write(str(type_num[i]))
        outputFile.write(',')
        outputFile.write(",".join('%s' % id for id in clunew[i].tolist()))
        outputFile.write('\n')

        for k in Target_types[i]:
            outputFile.write(",".join('%s' % id for id in k))
            outputFile.write('\n')
    outputFile.close()
    # 绘制分类结果

    scatterColors = ['red', 'green', 'yellow', 'black', 'purple', 'orange', 'brown', 'blue']
    for i in range(clusterNum):
        color = scatterColors[i % len(scatterColors)]
        x1 = []
        y1 = []
        for j in range(nPoints):
            if clusterRes[j] == i:
                x1.append(data[j][1])
                y1.append(data[j][2])
        plt.scatter(x1, y1, c=color, alpha=1, marker='p', s=100)

    #plt.scatter(clunew[:, 0].tolist(), clunew[:, 1].tolist(), c='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('cluster')
    plt.show()

    #task_match()
if __name__ == '__main__':
    k = 2                                          # 类别个数
    data = load_data()
    clu = random.sample(data, k)  # 随机取质心
    clu = np.asarray(clu)
    clu = clu[:, 1:3]
    clu = clu.astype(np.float_)
    err, clunew,  k, clusterRes= classfy(data, clu, k)
    while np.any(abs(err)) > 50:
        print(clunew)
        err, clunew,  k, clusterRes= classfy(data, clunew, k)

    clulist = cal_dis(data, clunew, k)
    clusterResult = divide(data, clulist)

    plotRes(data, clusterResult, clunew, k)
