# coding:utf-8
# /**
#  * date: 2020-04-08
#  * 有 m 个糖果和 n 个孩子。我们现在要把糖果分给这些孩子吃，但是糖果少，孩子多（m < n），
#  * 所以糖果只能分配给一部分孩子。每个糖果的大小不等，这 m 个糖果的大小分别是s1，s2，s3，……，sm。
#  * 除此之外，每个孩子对糖果大小的需求也是不一样的，只有糖果的大小大于等于孩子的对糖果大小的需求的时候，
#  * 孩子才得到满足。假设这 n 个孩子对糖果大小的需求分别是 g1，g2，g3，……，gn。
#  * 那么如何分配糖果，能尽可能满足最多数量的孩子呢?
#  */

# /**
#  * 求解：这道题如果用贪心来解解题思路还是比较明显的，对于每个小孩的需求 gn，
#  * 只要给他所有大小大于 gn 的糖果中的最小值即可，这样就能把更大的糖果让给需求更大的小孩。
#  */


class candy_and_children:
    def __init__(self):
        pass

    def candy_and_children(self, g_list, s_list):
        print(sorted(g_list))
        print(sorted(s_list))
        max_num = 0
        for i in range(0, len(g_list)):
            for j in range(0, len(s_list)):
                if s_list[j] >= g_list[i]:
                    max_num += 1
                    s_list[j] = -1
                    break
        return max_num


if __name__ == "__main__":
    cac = candy_and_children()
    g_list = [1, 4, 2, 6]
    s_list = [3, 1, 2, 7]
    result = cac.candy_and_children(g_list, s_list)
    print(result)
    pass
