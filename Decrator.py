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










