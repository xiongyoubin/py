# 场景：如果有30个函数，老板想测试这30个函数所需要的时间，如果一个一个函数加测试时间的代码，
# 不仅改变源代码，而且也使得代码重复，并且别的业务员调用函数方式也要改，因此为解决这个痛点
# 装饰器就是，在不改变原来代码的情况下，加了新的功能，并且还不改变调用方式，具体如下

import  time

def f() :
    print('f.....')

def bar() :
    print('666')

def show_time(f) :

    def inner():
        start = time.time()
        f()
        time.sleep(2)
        end = time.time()
        print('花了时间为%d秒'%(end-start))
    # 需要返回一个inner函数否则报：'NoneType' object is not callable
    return inner
f = show_time(bar)
f()

#高逼格的方式 @show_time 等价于 f = show_time(f)
# 调用机制是，show_time会找到foo函数，赋值变量为，使得 foo = show_time（foo）
@show_time
def foo() :
    print('f.....')
foo()


# 现在如果有新的函数add（x，y）带形参，将功能函数加定长参数
# 对装饰器调用机制的加深理解的例子
def show_time1(f) :
    def inner(x,y):
        start = time.time()
        f(x,y)
        time.sleep(2)
        end = time.time()
        print('花了时间为%d秒'%(end-start))
    return  inner
@show_time1
# 将功能函数add传参改变以后相应的inner函数也要改
# 因为装饰器首先走 add = show_time1（add），因此先拿到inner函数，inner函数要将add的两个参数带上
# 以上为装饰器的调用流程
def add(x,y):
    print(x+y)
add(1,2)


# 不定长累加,将功能函数加不定长参数
# add(1,2,3,4,5)
def show_time2(f) :
    def inner(*x,**y):
        start = time.time()
        f(*x,**y)
        time.sleep(3)
        end = time.time()
        print('花了时间为%d秒'%(end-start))
    return  inner
@show_time2
def add(*a,**b):
    s=0
    for i in a:
        s = s +i
    print(s)
add(1,2,3,4,5)
# 装饰器参数
# 给装饰器传入参数（相当于给装饰器加一个闭包，从外面加入一个参数）flag
# 场景1：如果我想给foo函数打印日志记录，但是不想让bar函数打印日志记录
def logger(flag='false'):
    def show_time1(f):
        def inner(x, y):
            start = time.time()
            f(x, y)
            time.sleep(2)
            end = time.time()
            print('花了时间为%d秒' % (end - start))
            if flag == 'ture':
                print('打印日志记录')
        return inner
    return show_time1
@logger('ture')   #相当于 @show_time1，加了一个闭包，通过闭包传参数
def add(x,y):
    print(x+y)
add(1,2)














