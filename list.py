list = [1,'sdfds',1.0]


###get
print(list[0])
print(list[1])
print(list[2])

print(list[-1])
print(list[-2])
print(list[-3])


##add
list.insert(0,0)
list.append('final')
print(list)

##delete
list.remove('final')
#list.remove(-1)
print(list)

##删除指定的index
print(list.pop())  ##最后
print(list.pop(1))

###多元数组，可以动态增加
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(len(s))

###nul
list_null = []
print(list_null)
