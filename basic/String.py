####在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

print('中国')
print(ord('中'))
print(chr(ord('中')+1))


print('ABC'.encode('ascii'))
print('中国'.encode('utf-8'))
print( b'ABC'.decode('utf-8'))

print(len('ABC'))  ###3个字符
print(len('中国龙')) ###3个字符
print(len(b'ABC'))   ###3个字节
print(len('中国'.encode('utf-8')))  ###6个字节

#ch = 0
#while ch <= 65535:
 #   print(ch,chr(ch))
  #  ch = ch + 1

print('%s==>%s'%('final',"tracy"))