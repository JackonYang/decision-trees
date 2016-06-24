# -*- coding:utf-8 -*-
import math

def info_i(p):
    """香农的信息公式, 物理中又叫做熵
    
    处于某一个分类的概率越高, 信息越多
    """
    return p and -math.log(p, 2)


def info(*p):
    """所有分类的信息期望值

    """
    return sum([i*info_i(i) for i in p])


if __name__ == '__main__':
    print info(0.5, 0.5)
    print info(0.67, 0.33)
    print info(1, 0)
