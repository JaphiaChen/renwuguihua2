import numpy as np


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