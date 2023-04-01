

### 可变数据类型

基本的数据类型：数字型、字符串、元祖、列表、字典、集合
不可变数据类型：数字型、字符串、元祖
可变数据类型：列表、字典、集合



### 闭包

在一个外函数内定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用，这样就构成了一个**闭包**。

```python
# 闭包函数的实例：outer()是外部函数，a和b都是外部函数的临时变量
def outer(a):
    b = 10
    # inner()是内部函数
    def inner():
        # 在内部函数中用到了外部函数的临时变量
        print(a+b)
    # 外部函数返回值是内部函数的引用
    return inner

# 调用外部函数，传入参数5。此时外函数两个临时变量a是5 b是10，并创建了内部函数，然后把内部函数的引用返回给了demo进行存储，外部函数结束的时候发现内部函数将会调用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
demo1 = outer(5)
# demo存储了外部函数的返回值，也就是inner()函数的引用，这里相当于执行inner函数
demo1()     # 15

demo2 = outer(7)
demo2()     # 17
```

在闭包中，内层函数可以访问外层函数的变量(闭包变量)，但是不可写，除非使用nonlocal关键字、或者外层函数的变量是可变数据类型

```python
# 修改闭包变量实例
def outer(a):  # outer是外部函数，a和b都是外部函数的临时变量
    b = 10  # a和b都是闭包变量
    c = [a]  # 这里对应修改闭包变量的方法2
    def inner():  # inner是内部函数
        # # 内函数中想修改闭包变量
        # nonlocal b  # 方法1 nonlocal关键字声明
        # b += 1
        #
        c[0] += 1  # 方法2 把闭包变量修改成可变数据类型，比如：列表
        print(c[0], b)
    return inner  # 外部函数返回内部函数的引用
demo = outer(5)
demo()  # 6 10
```

使用闭包的过程中，一旦外部函数被调用一次返回了内部函数的引用，虽然每次调用内部函数是开启一个函数执行过后消亡，但是闭包变量实际上只有一份，每次开启内部函数都在使用同一份闭包变量

```Python
def outer(x):
    def inner(y):
        nonlocal x
        x += y
        return x
    return inner

demo = outer(10)
print(demo(1), demo(3))     # 11    14
```

#### 闭包的意义

闭包可以用来在一个函数与一组“私有”变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能够保持其持久性。





### 装饰器

函数装饰器

```Python
@dec
def f():
    pass
# 等价于：
f = dec(f) # 这里的@后面省略了括号


@dec(x)
def f():
    pass
#等价于
f = dec(x)(f)


@dec2
@dec1(x)
def f():
    pass

#等价于
f = dec2(dec1(x)(f))
```



作用在类上的装饰器

```Python
def decorator(func):
    def inner(*args, **kwargs):
        print("decorator")
        return func(*args, **kwargs)

    return inner

@decorator
class A:
    pass

A = decorator(A)()  # 和上面的写法完全一样
```



装饰器本身就是类

```Python
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('decorator')
        return self.func(*args, **kwargs)


@Decorator
def a():
    print('a')

a = Decorator(a)()  # 和上面的写法完全一样
```

