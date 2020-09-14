# 无参数函数
def say_hello():
    print('Hello!')


say_hello()


# 有参数函数
def greetings(x):
    print(x)


greetings("Good morning!")


# 返回0个值或者没有return:返回None
def func():
    pass


a = func()
print(a, type(a))


# 返回1个值:返回的就是该值本身
def func1():
    return 123


b = func1()
print(b, type(b))


# 返回多个值: 多个返回值用逗号分隔开,返回的是元组形式
def func2():
    return 1, 1.1, 'hello', [1, 2, 3]


c = func2()
print(c, type(c))


# 函数内可以有多个return,但只要执行一次,整个函数就立即结束,并且将return后的值返回
def func3():
    print(1)
    return
    print(2)
    return
    print(3)


func3()
