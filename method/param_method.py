def power(x):
    return x * x


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

###默认值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

###list
def add_end(L=[]):
    L.append('END')
    return L

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

###可变的参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1,2,3]
calc(*nums)

###关键函数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


##递归函数
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)