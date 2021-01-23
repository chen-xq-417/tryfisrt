"""
list_1=[i*j for i in range(1,4)  for j in range(1,4) ]
print(list_1)


tuple_1 = (1,2,3)
tuple_2 = 1,2,3
print("tuple_1",tuple_1)
print(type(tuple_1))


name ='lili'
age =20
list1 = [1,2,3]
dict1 = {'name':'tom','gender':'male'}
print('my list is {},dict is {}'.format(list1,dict1))
print('my name is {},age is {}'.format(name,age))
print('my name is {1},age is {0}'.format(name,age))


namelist = ['lili','tom','jerry']
dict1 = {'name':'tom','gender':'male'}
print('we name:{} {} and {}'.format(*namelist))
print('my name is:{name},my gender is:{gender}'.format(**dict1))



name ='lili'
age =20
list1 = [1,2,3]
dict1 = {'name':'tom','gender':'male'}
print(f'my name is {name},age is {age},my list is {list1[0]}')
print(f'my name is {name.upper()}')

#文件打开/操作/关闭
print(open(('data.txt')))

f = open('data.txt')
print(f.readable())
#print(f.readlines())
print(f.readline())
f.close()

#with 语句快，可以将文件打开后，操作完毕，自动关闭这个文件
with open('data.txt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break


import json
data={
    'name':'jerry',
    'age':26,
    'gender':'female'
}

data1 = json.dumps(data)
print(data1)
print(type(data1))

data2 = json.loads(data1)
print(type(data2))


for  i in range(1,31):
    print(sheet_ranges.cell((column=1, row=1).value))

#yaml
import yaml

with open ("demo3.yml","w") as f:
    yaml.dump(data={'a': [1, 2]}, stream=f)


"""
