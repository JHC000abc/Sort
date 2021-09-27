import datetime
import time

def wrapper(func):
    def time_record():
        func()
        start_time=datetime.datetime.now()
        print(str(start_time).split('.')[0])

    return time_record()

@wrapper
def test01():
    print('test01正在执行')
    print('当前时间为:',end='')


@wrapper
def test02():
    print('test02正在执行')
    print('当前时间为:',end='')



if __name__=='__main__':
    test01
    test02




