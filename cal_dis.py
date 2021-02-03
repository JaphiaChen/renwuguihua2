import numpy as np
import math as m


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
