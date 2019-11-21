# coding:utf-8
# eg matrix
matrix = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0]]
# 四种类型，对每种类型设置一个占位符，即往该方向已占用
placer = [0, 0, 0, 0]

# 凌乱的想法
# 1.当1的元素个数大于方阵的行列数时，则没有这么一条直线
# 2.只要1的元素个数大于0，就有一条直线
# 将
def dist_1(matrix):
    # matrix_tmp = matrix
    dist = 0
    N = len(matrix[0])
    for i in range(N):
        for j in range(N):
            # print(matrix[i][j])
            if placer[i] == 0 and matrix[i][j] == 1:
                # matrix_tmp[i][0] = 1
                # matrix_tmp[i][j] = 0
                print("s从(%d,%d)移到(%d,%d)" % (i, j, i, 0))
                dist += j
                placer[i] = 1
            elif placer[i] == 1 and matrix[i][j] == 1:
                if i < N-1:
                    # matrix_tmp[i][j] = 0
                    # matrix_tmp[i+1][0] = 1
                    print("从(%d,%d)移到(%d,%d)" % (i, j, i+1, 0))
                    dist += (j+1)
                    placer[i+1] = 1
                else:
                    for k in range(i,-1,-1):
                        # print(k)
                        if placer[k]==0:
                            print("从(%d,%d)移到(%d,%d)" % (i, j, k, 0))
                            dist += (j+1)
                            placer[k] = 1

    # print(matrix_tmp)
    print("移动距离为：%d" % dist)
    return dist

# def function(matrix):


dist_1(matrix)
