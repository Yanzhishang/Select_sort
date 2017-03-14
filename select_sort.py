#coding=utf-8
import random
#定义三个常量来表示随机数组的下限、上限和长度
start = 1
stop = 1000
length = 100
#定义一个空数组来存放生成的随机数
list = []
#生成随机数的方法
def random_list():
    for i in range(length):
        #把随机数插入到数组中
        list.append(random.randint(start,stop))
    return list
print("随机的数组为：",random_list())

#选择排序
for i in range(len(list) - 1):
    min = i   #从无序数组中选出最小的赋给min
    for j in range((i + 1), len(list)):
        if list[j] < list[min]:
            min = j
    (list[i], list[min]) = (list[min], list[i])

print("排序后数组为：",list)


#时间复杂度：O（n^2）
#空间复杂度：O（1）
