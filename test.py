'''
1 从python的list(列表)中随机抽取5个元素，写出尽可能多的方法。
'''
import random

list=['1','2','3','4','5','6']
# 无重复
print(random.sample(list,k=5))
# 有重复
print(random.choices(list,k=5))
# random index
li=[]
for i in range(1,4):
    index=random.randint(0,len(list)-1)
    li.append(index)
print(li)
for x in (li):
    print(list[x])



print('\"'*50)
'''
2 <div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class属性“nam”是不确定的，也可能是别的值。
'''
import re
str = '<div class="nam">中国</div>'
lis = re.findall('<div class=".*">(.*?)</div>',str)
print(lis)
print('\"'*50)
'''
3 有3个数组/list，已经从小到大排序，将3个数组归并到一个数组中，要求从小到大排序。需要写出具体的代码，语言不限。
'''

list1 = [3, 4, 5, 6]
list2 = [8, 9, 10, 11,13]
list3 = [10, 12, 13, 14,15, 18]

list1.extend(list2)

list1.extend(list3)
# print(list1)
arr=[]
for i in set(list1):
    arr.append(i)
arr.sort()
print(arr)

print('\"'*50)


'''
4 搜索引擎一天产生约1亿条用户搜索记录（格式为一行一个搜索词），快速求出搜索频率最高的top10搜索词。需要写出具体的代码，语言不限。
'''
"没做过，不会"

'''
5 mysql基本操作。
数据表 app_info，记录app的基本信息: 字段为app_id, title
数据表app_rank 记录app的排名信息：字段为app_id, rank(榜单排名)
需求，获得app_id, title，rank 并按照rank从小到大排序。写出mysql语句
'''

# select * from app_info inner join (select * from app_rank) as F ON app_info.app_id=F.app_id order by F.rank

import math
print(type(math.pow(2,4)))

print(hash(1))
print(hash(1.0))    # 相同的数值，不同类型，哈希值是一样的
print(hash("abc"))
print(hash("ABC"))
print(hash("hello world"))
print('\"'*50)

# import hashlib
#
# md5 = hashlib.md5()  # 应用MD5算法
# data = "hello world"
# md5.update(data.encode('gbk'))
# print(md5.hexdigest())
# md5.update(data.encode('utf8'))
# print(md5.hexdigest())


