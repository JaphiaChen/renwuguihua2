from cal_dis import cal_dis
from divide import divide
from center import center


def classfy(data, clu, k):
    """
    迭代收敛更新质心
    :param data: 样本集合
    :param clu: 质心集合
    :param k: 类别个数
    :return: 误差，新质心，类别个数，分类结果
    """
    clulist = cal_dis(data, clu, k)
    clusterRes = divide(data, clulist)
    clunew= center(data, clusterRes, k)
    err = clunew - clu
    return err, clunew, k, clusterRes
