list_ = ['jxilong', 'final']
for element in list_:
    print(element)


array = ('final','final')
for element in array:
    print(element)

print(range(5))
array = list(range(5))
print(array)


sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
x = 1
while x < 101:
    sum = sum + x
    x = x+1
print(sum)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue
        #continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

    if n == 9:
        break