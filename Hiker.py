# coding:utf-8
import numpy as np


# mtx_list_1 = [[0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
# mtx_list_2 = [[0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]

# matrix=np.array(mtx_list_1)


import numpy as np


class Hiker:
            
    def find_center(self,mtx_arr):
        # 将二维list转为二维的ndarray，为了加快对矩阵的操作
        # 将矩阵中为1的值的坐标保存在一个ndarray中
        value_one_arr=np.argwhere(mtx_arr==1)
        # NUM_OF_1为该矩阵中为1的元素的个数
        NUM_OF_1=len(value_one_arr)
        # 对每个为1的元素的坐标做好映射，用一个字典来存储key：标号，value：坐标值
        loc_dict={}
        for i in range(NUM_OF_1):
            loc_dict[i]=value_one_arr[i]
        # 建立一个二维ndarray来存储每个为1的元素之间的坐标的距离
        dist_of_1= np.zeros((NUM_OF_1,NUM_OF_1))
        for i in range(0,dist_of_1.shape[0]):
            for j in range(0,dist_of_1.shape[1]):
                dist_of_1[i][j]=np.sum(np.abs(loc_dict[i]-loc_dict[j]))
                # print(dist_of_1[i][j])
        # 对每列进行求和，得出最小值并获取他的下标
        min_of_dist=float("inf")
        min_idx=0
        for i in range(NUM_OF_1):
            col_sum=np.sum(dist_of_1[i], axis=0)
            if col_sum<min_of_dist:
                min_of_dist=col_sum
                min_idx=i
        min_loc=loc_dict[min_idx].tolist()
        # print(min_loc)
        # 获取中心下标，并对到他的距离的点进行排序
        print(dist_of_1)
        print(min_idx)
        # 对最小值所在的下标的那列进行排序
        sorted_idx_ndarr=np.argsort(dist_of_1[min_idx])
        # print("sorted_idx_ndarr:",type(sorted_idx_ndarr))
        return min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx
                
    def center_extend_vertical(self,mtx_arr,min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx,num_of_1,N):
        print("进入垂直方向中心扩展算法：")
        move_actions_vertical=[]
        step_dict={}
        # print("min_loc:",min_loc)
        # print(min_loc[0],min_loc[1])
        sum_steps=0
        flag_list=[0]*N
        # 根据中心扩展 按照垂直方向扩展
        # 以各个点离他最近的点min_loc为中心进行垂直方向扩展
        flag_list[min_loc[0]]=1
        # 定义两个指针 一个往上走 一个往下走，初始化两个指针，初始化值均为中心点的行值
        up_point=min_loc[0]
        down_point=min_loc[0]
        # sorted_idx_ndarr的第一个元素就是中心点本身，所以跳过
        for i in range(1,len(sorted_idx_ndarr)):
            # print(sorted_idx_ndarr[i])
            current_x=loc_dict[sorted_idx_ndarr[i]].tolist()[0]
            current_y=loc_dict[sorted_idx_ndarr[i]].tolist()[1]
            # print(current_x,current_y)
            # while up_point!=0 and down_point!=N-1:
            # 如果坐标在中心点上方，就往上走
            if current_x<=min_loc[0]:
                # print("up_point:%d"%up_point)
                # 如果上方满了，就往下走
                if up_point-1<0:  #up_point永远指向的flag_list为1
                    down_point+=1
                    flag_list[down_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, down_point, min_loc[1]))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=down_point
                    step_dict['col_to']=min_loc[1]
                    move_actions_vertical.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-down_point)+abs(current_y-min_loc[1]))
                # 如果上方没满，就继续往上走
                else:
                    up_point-=1
                    flag_list[up_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, up_point, min_loc[1]))  
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=up_point
                    step_dict['col_to']=min_loc[1]
                    move_actions_vertical.append(step_dict) 
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-up_point)+abs(current_y-min_loc[1]))        
            # 如果坐标在中心点下方，就往下走
            elif current_x>min_loc[0]:
                # print("down_point:%d"%down_point)
                # 如果下方满了，就往上走
                if down_point+1>N-1:  #down_point永远指向的flag_list为1
                    up_point-=1
                    flag_list[up_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, up_point, min_loc[1]))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=up_point
                    step_dict['col_to']=min_loc[1]
                    move_actions_vertical.append(step_dict) 
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-up_point)+abs(current_y-min_loc[1]))
                # 如果下方没满，就往继续往下走
                else:
                    down_point+=1
                    flag_list[down_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, down_point, min_loc[1]))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=down_point
                    step_dict['col_to']=min_loc[1]
                    move_actions_vertical.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-down_point)+abs(current_y-min_loc[1]))

        print("sum_steps:%d"%sum_steps)
        return sum_steps,move_actions_vertical

    def center_extend_level(self,mtx_arr,min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx,num_of_1,N):
        print("进入水平方向中心扩展算法：")
        move_actions_level=[]
        step_dict={}
        # print("min_loc:",min_loc)
        # print(min_loc[0],min_loc[1])
        sum_steps=0
        flag_list=[0]*N
        # 根据中心扩展 按照水平方向扩展
        # 以各个点离他最近的点min_loc为中心进行水平方向扩展
        flag_list[min_loc[1]]=1
        # 定义两个指针 一个往左走 一个往右走，初始化两个指针，初始化值均为中心点的列值
        left_point=min_loc[0]
        right_point=min_loc[0]
        # sorted_idx_ndarr的第一个元素就是中心点本身，所以跳过
        for i in range(1,len(sorted_idx_ndarr)):
            # print(sorted_idx_ndarr[i])
            current_x=loc_dict[sorted_idx_ndarr[i]].tolist()[0]
            current_y=loc_dict[sorted_idx_ndarr[i]].tolist()[1]
            # print(current_x,current_y)
            # 如果坐标在中心点左边，就往左走
            if current_y<=min_loc[1]:
                print("left_point:%d"%left_point)
                # 如果左边满了，就往右走
                if left_point-1<0:  #left_point永远指向的flag_list为1
                    right_point+=1
                    flag_list[right_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, min_loc[0], right_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=min_loc[0]
                    step_dict['col_to']=right_point
                    move_actions_level.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-min_loc[0])+abs(current_y-right_point))
                # 如果上方没满，就继续往上走
                else:
                    left_point-=1
                    flag_list[left_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, min_loc[0], left_point)) 
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=min_loc[0]
                    step_dict['col_to']=left_point
                    move_actions_level.append(step_dict)  
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-min_loc[0])+abs(current_y-left_point))        
            # 如果坐标在中心点下方，就往下走
            elif current_y>min_loc[1]:
                # print("right_point:%d"%right_point)
                # 如果右边满了，就往左走
                if right_point+1>N-1:  #right_point永远指向的flag_list为1
                    left_point-=1
                    flag_list[left_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, min_loc[0], left_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=min_loc[0]
                    step_dict['col_to']=left_point
                    move_actions_level.append(step_dict) 
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-min_loc[0])+abs(current_y-left_point))
                # 如果下方没满，就往继续往下走
                else:
                    right_point+=1
                    flag_list[right_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, min_loc[0], right_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=min_loc[0]
                    step_dict['col_to']=right_point
                    move_actions_level.append(step_dict) 
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-min_loc[0])+abs(current_y-right_point))

        print("sum_steps:%d"%sum_steps)
        return sum_steps,move_actions_level

    def center_extend_leftslash(self,mtx_arr,min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx,num_of_1,N):
        print("进入撇方向中心扩展算法：")
        move_actions_leftslash=[]
        step_dict={}
        # print("min_loc:",min_loc)
        # print(min_loc[0],min_loc[1])
        sum_steps=0
        flag_list=[0]*N
        # 这种移动策略不是最优的 后续优化
        # 根据中心扩展 按照撇方向扩展
        # 将min_loc按列方向移到矩阵中心
        print("从(%d,%d)移到(%d,%d)" % (min_loc[0], min_loc[1], min_loc[0], N-1-min_loc[0]))
        step_dict['row_from']=min_loc[0]
        step_dict['col_from']=min_loc[1]
        step_dict['row_to']=min_loc[0]
        step_dict['col_to']=N-1-min_loc[0]
        move_actions_leftslash.append(step_dict)
        sum_steps+=abs(min_loc[1]-(N-1-min_loc[0]))
        # 以各个点离他最近的点min_loc为中心进行撇方向扩展
        flag_list[min_loc[0]]=1
        # 定义两个指针 一个往撇上走 一个往撇下走，初始化两个指针，初始化值均为中心点的行值
        up_point=min_loc[0]
        down_point=min_loc[0]
        # sorted_idx_ndarr的第一个元素就是中心点本身，所以跳过
        for i in range(1,len(sorted_idx_ndarr)):
            # print(sorted_idx_ndarr[i])
            current_x=loc_dict[sorted_idx_ndarr[i]].tolist()[0]
            current_y=loc_dict[sorted_idx_ndarr[i]].tolist()[1]
            # print(current_x,current_y)
            # 如果坐标在中心点上方，就往撇上走
            if current_x<=min_loc[0]:
                # print("up_point:%d"%up_point)
                # 如果上方满了，就往下走
                if up_point-1<0:  #up_point永远指向的flag_list为1
                    down_point+=1
                    flag_list[down_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, down_point, N-1-down_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=down_point
                    step_dict['col_to']=N-1-down_point
                    move_actions_leftslash.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-down_point)+abs(current_y-(N-1-down_point)))
                # 如果上方没满，就继续往上走
                else:
                    up_point-=1
                    flag_list[up_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, up_point, N-1-up_point))   
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=up_point
                    step_dict['col_to']=N-1-up_point
                    move_actions_leftslash.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-up_point)+abs(current_y-(N-1-up_point)))        
            # 如果坐标在中心点下方，就往下走
            elif current_x>min_loc[0]:
                # print("down_point:%d"%down_point)
                # 如果下方满了，就往上走
                if down_point+1>N-1:  #down_point永远指向的flag_list为1
                    up_point-=1
                    flag_list[up_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, up_point, N-1-up_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=up_point
                    step_dict['col_to']=N-1-up_point
                    move_actions_leftslash.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-up_point)+abs(current_y-(N-1-up_point)))
                # 如果下方没满，就往继续往下走
                else:
                    down_point+=1
                    flag_list[down_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, down_point, N-1-down_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=down_point
                    step_dict['col_to']=N-1-down_point
                    move_actions_leftslash.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-down_point)+abs(current_y-(N-1-down_point)))

        print("sum_steps:%d"%sum_steps)
        return sum_steps,move_actions_leftslash

    def center_extend_backslash(self,mtx_arr,min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx,num_of_1,N):
        print("进入捺方向中心扩展算法：")
        move_actions_backslash=[]
        step_dict={}
        # print("min_loc:",min_loc)
        # print(min_loc[0],min_loc[1])
        sum_steps=0
        flag_list=[0]*N
        # 这种移动策略不是最优的 后续优化
        # 根据中心扩展 按照捺方向扩展
        # 将min_loc按列方向移到矩阵中心
        print("从(%d,%d)移到(%d,%d)" % (min_loc[0], min_loc[1], min_loc[0], min_loc[0]))
        step_dict['row_from']=min_loc[0]
        step_dict['col_from']=min_loc[1]
        step_dict['row_to']=min_loc[0]
        step_dict['col_to']=min_loc[0]
        move_actions_backslash.append(step_dict)
        sum_steps+=abs(min_loc[1]-min_loc[0])
        # 以各个点离他最近的点min_loc为中心进行捺方向扩展
        flag_list[min_loc[0]]=1
        # 定义两个指针 一个往捺上走 一个往捺下走，初始化两个指针，初始化值均为中心点的行值
        up_point=min_loc[0]
        down_point=min_loc[0]
        # sorted_idx_ndarr的第一个元素就是中心点本身，所以跳过
        for i in range(1,len(sorted_idx_ndarr)):
            # print(sorted_idx_ndarr[i])
            current_x=loc_dict[sorted_idx_ndarr[i]].tolist()[0]
            current_y=loc_dict[sorted_idx_ndarr[i]].tolist()[1]
            # print(current_x,current_y)
            # 如果坐标在中心点上方，就往捺上走
            if current_x<=min_loc[0]:
                # print("up_point:%d"%up_point)
                # 如果上方满了，就往下走
                if up_point-1<0:  #up_point永远指向的flag_list为1
                    down_point+=1
                    flag_list[down_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, down_point, down_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=down_point
                    step_dict['col_to']=down_point
                    move_actions_backslash.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-down_point)+abs(current_y-down_point))
                # 如果上方没满，就继续往上走
                else:
                    up_point-=1
                    flag_list[up_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, up_point, up_point))  
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=up_point
                    step_dict['col_to']=up_point
                    move_actions_backslash.append(step_dict) 
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-up_point)+abs(current_y-up_point))        
            # 如果坐标在中心点下方，就往下走
            elif current_x>min_loc[0]:
                # print("down_point:%d"%down_point)
                # 如果下方满了，就往上走
                if down_point+1>N-1:  #down_point永远指向的flag_list为1
                    up_point-=1
                    flag_list[up_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, up_point, up_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=up_point
                    step_dict['col_to']=up_point
                    move_actions_backslash.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-up_point)+abs(current_y-up_point))
                # 如果下方没满，就往继续往下走
                else:
                    down_point+=1
                    flag_list[down_point]=1
                    print("从(%d,%d)移到(%d,%d)" % (current_x, current_y, down_point, down_point))
                    step_dict['row_from']=current_x
                    step_dict['col_from']=current_y
                    step_dict['row_to']=down_point
                    step_dict['col_to']=down_point
                    move_actions_backslash.append(step_dict)
                    # 计算总共走的步数 
                    sum_steps+=(abs(current_x-down_point)+abs(current_y-down_point))

        print("sum_steps:%d"%sum_steps)
        return sum_steps,move_actions_backslash

    def center_extend(self,mtx_arr,num_of_1,N):
        result_dict={}
        min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx=self.find_center(mtx_arr)
        sum_steps_vertical,move_actions_vertical=self.center_extend_vertical(mtx_arr,min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx,num_of_1,N)
        sum_steps_level,move_actions_level=self.center_extend_level(mtx_arr,min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx,num_of_1,N)
        sum_steps_leftslash,move_actions_leftslash=self.center_extend_leftslash(mtx_arr,min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx,num_of_1,N)
        sum_steps_backslash,move_actions_backslash=self.center_extend_backslash(mtx_arr,min_of_dist,min_loc,sorted_idx_ndarr,loc_dict,min_idx,num_of_1,N) 
        result_dict[sum_steps_vertical]=move_actions_vertical
        result_dict[sum_steps_level]=move_actions_level
        result_dict[sum_steps_leftslash]=move_actions_leftslash
        result_dict[sum_steps_backslash]=move_actions_backslash
        min_steps=min(sum_steps_vertical,sum_steps_level,sum_steps_leftslash,sum_steps_backslash)
        # print(min_steps)
        move_actions=result_dict[min_steps]
        # print(move_actions)
        return move_actions

    def function(self,matrix):
        # matrix是np矩阵
        move_actions=[]
        N=len(matrix[0])
        # 根据1的个数分情况讨论
        num_of_1= np.sum(matrix==1)
        if num_of_1==0:
            print("矩阵中没有1，不存在这么一条直线")
        elif num_of_1>N:
            print("1的个数大于矩阵列值，因此不存在这么一条直线")
        else:
            print("1的个数在0-N之间，因此存在这么一条直线")
            move_actions=self.center_extend(matrix,num_of_1,N)
        return move_actions
    
    def draw_line(self, matrix):
        """
        参赛选手实现该函数，使得01矩阵的所有1排成一条直线
        :param matrix 100*100的01矩阵
        :return: 矩阵元素的置换次序move_actions,是形如[{'row_from': 67, 'col_from': 23, 'row_to': 68, 'col_to': 23}, ...]这样由转换dict组成的list
        """
        move_actions = []
        move_actions=self.function(matrix)

        return move_actions

    

# if __name__ == "__main__":
#     hiker=Hiker()
#     hiker.draw_line(matrix)
#     pass
