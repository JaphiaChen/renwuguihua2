import matplotlib.pyplot as plt


def plotRes(data, clusterRes, clunew, clusterNum):
    """
    结果输出和结果可视化
    :param data:样本集
    :param clusterRes:聚类结果
    :param clunew:新质心
    :param clusterNum: 类个数
    :return:
    """
    nPoints = len(data)

    # 输出分类结果
    Target_types = []
    type_num =[]
    outputFile = open('cluster_result.txt', mode='a+')
    outputFile.seek(0,0)
    outputFile.truncate()
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
    scatterColors = ['red', 'green', 'yellow', 'black',  'purple', 'orange', 'brown', 'blue']
    for i in range(clusterNum):
        color = scatterColors[i % len(scatterColors)]
        x1 = []
        y1 = []
        for j in range(nPoints):
            if clusterRes[j] == i:
                x1.append(data[j][1])
                y1.append(data[j][2])
        plt.scatter(x1, y1, c=color, alpha=1, marker='p', s=100)

    #plt.scatter(clunew[:, 0].tolist(), clunew[:, 1].tolist(), c='blue')    #绘制质心
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('cluster')
    plt.show()
