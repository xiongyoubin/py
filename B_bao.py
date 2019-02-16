
# 导入这个foo只是想把函数导入进来，不需要执行函数，或者该文件的测试代码
# foo是文件名，hello（）是这个文件名里面的一个函数
import foo
foo.hello()

# 闭包的定义,对于一个内部函数(inner()),对在外部的作用域，进行了一个引用（X）所谓引用就是print（x）
# 所以这个内部函数inner就是一个闭包，因此闭包是符合两个条件的一个函数
def outter () :
    x = 10   #条件一：外部作用域（但不是全局作用域）
    def inner():   #条件二 ：内部函数
        print(x)
    return inner #结论：闭包
# 执行inner里面的程序要怎么调用
# 方式一，outter拿到的是inner函数
f = outter()
# 这个实在outter外面（外面就是没有四个空格）执行函数，
# f()执行的是
#         def inner():
#             print(x)
f()
# 方式二,因为inner（）是局部变量，虽然是函数但是也是变量，是局部变量
# 局部变量在全局不可以直接调用，但是如果是闭包的话就可以直接调用


# python机制的理解
def ff():
    c=5
# 当函数启用ff()函数时候c=5就已经不能被除函数以外的东西调用
ff()
# 打印c没有用了，因为c=5，已经被函数调用失效了

# 闭包的第二种形式,以形式参数的形式被调用也属于闭包
def outter2(b):
    def inner2():
        print(b)
h = outter2(2)
h


