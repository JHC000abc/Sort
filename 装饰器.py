# import datetime
# import time
#
# def wrapper(func):
#     def time_record():
#         func()
#         start_time=datetime.datetime.now()
#         print(str(start_time).split('.')[0])
#
#     return time_record()
#
# @wrapper
# def test01():
#     print('test01正在执行')
#     print('当前时间为:',end='')
#
#
# @wrapper
# def test02():
#     print('test02正在执行')
#     print('当前时间为:',end='')
#
#
#
# if __name__=='__main__':
#     test01
#     test02
#
#
#
#
# import re
# import sys
# str = 'ajskdlaslkdjbnnmnv,mxncmvnx,mssbbbbnkfnsklnflnslkdlsldlsbb'
# print(str)
# print(re.sub('b+', 'b', str))
#
# str2 = '  as                 jdk   sd  '
# print(str2)
# # 将多个空格替换成一个空格
# print(re.sub(' +',' ',str2))
# # 将多个空格全部替换成一个空格
# print(' '.join(str2.split()))
# # 将多个空格全部替换成一个空格
# print(re.sub(' +',' ',str2).lstrip().rstrip())
# # 查看引用计数
# print(sys.getrefcount(str2))
# # 输出内建方法
# print(dir(list))
# print(dir(dict))
# print(dir(tuple))
# print(dir(int))
# print(dir(bool))
# print(dir(set))
# print('='*40)
# import sys
# for i in range(10):
#     print(i)
#
#     print(sys.getrefcount(i))

# def jiecheng(n):
#     result=1
#     if n<0:
#         print('异常')
#     elif n==0:
#         print(0)
#     else:
#         for i in range(1,n+1):
#             result*=i
#         print(result)
#
# jiecheng(10)

# class A(object):
# 	_instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#             return cls._instance
#         else:
#             return cls._instance
import re
str='abcd[]\s\\t234afhhs254\s264sss  jakGHJsf56gfggfgggggfhhhhhhGH$JKG32%$ '
# 匹配 2.4 ['234', '254', '264']
re_result=re.findall('2[356]4',str)
re_result1=re.findall('\d',str)
re_result3=re.findall('\D',str)
re_result4=re.findall('\s',str)
re_result5=re.findall('\S',str)
re_result6=re.findall('\w',str)
re_result7=re.findall('\W',str)
re_result8=re.findall('fh*',str)
re_result9=re.findall('fh+',str)
re_result10=re.findall('fh{2}',str)

print(re_result)
print(re_result1)
print(re_result3)
print(re_result4)
print(re_result5)
print(re_result6)
print(re_result7)
print(re_result8)
print(re_result9)
print(re_result10)