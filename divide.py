import numpy as np


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
