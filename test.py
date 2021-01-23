"""
int_a =1
float_a = 2.1
complex_a = 2j

#通过type查看变量的数据类型
print(type(int_a))
print(type(float_a))
print(type(complex_a))

# \：转义符
# r：忽略转义符的作用
# + 以及空格：多个字符串连接
#切片
str_a = '12345'
print (str_a)

#[start:stop:step][开始：结束：步长]
print(str_a[0:5:2])

#列表
list1 = [1,2,3]
print (list1[0])
print (list1[:])


a = 'aaa'
d = 'ddd{}'
b = f'bbb{a}'
c = f'ccc{b}'
print(c)
print(d.format(a))

'''索引'''
list_a = [1,2,3,'a','b','c']
print(list_a[0])
print(list_a[-1])
print(list_a[0:3])#从0开始，显示三位

#多重分支
a = 4
if a == 0:
    print('a=0')
elif a == 1:
    print('a=1')
elif a == 2:
    print('a=2')
else:
    print('a谁都不等于')


#分段函数求值
       3x-5 （x>1）
f(x) = x+2   (1<=x<=1)
       5x+3  (x<-1)
#分支结构
x = -2
if x > 1:
    y=3*x-5
else:
    if x >= -1:
        y=x+2
    else:
        y=3*x-5
print(y)
"""
# 多重分支
x = -2
if x > 1:
    y = 3 * x - 5
elif 1 <= x <= 1:
    y = x + 2
elif x < -1:
    y = 5 * x + 3
print(y)
