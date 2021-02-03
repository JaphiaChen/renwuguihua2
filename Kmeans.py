import numpy as np
import random
from load_data import load_data
from classfy import classfy
from cal_dis import cal_dis
from divide import divide
from plotRes import plotRes
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
