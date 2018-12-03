def solution(T):
    # write your code in Python 3.6
    return min(len(T) // 2, len(set(T)))


# 糖果一人一半、其中一人可以拿最多種類的糖果是幾種
# T = [1,1,2,2,3,4]  -> 3 種
# T = [1,2,1,2,1,2]  -> 2 種