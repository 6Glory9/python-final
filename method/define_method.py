def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(1))


###空函数
def null_method():
    pass

print(null_method())

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(1.2))
print(my_abs(-2))


##返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print(move(100, 100, 60, math.pi / 6))