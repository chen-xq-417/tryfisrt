"""
#1.计算1～100，求和
result = 0
for i in range(101):
    result =result+i
print(result)

#2.加入分支结构实现1～100之间的偶数求和
result = 0
for i in range(101):
    if i%2==0:
        result =result+i
print(result)

#3.使用python实现1～100之间的偶数求和
result = 0
for i in range(2,101,2):
    result =result+i
print(result)

#猜数字游戏
#计算机出一个1～100之间的随机数由人来猜
#计算机根据人猜的数字分别给出提示
#大一点/小一点/猜对了
import random
computer_number = random.randint(1,100)
while True:
    person_number = int(input("请输入一个数字"))
    if person_number > computer_number:
        print ("小一点")
    elif person_number < computer_number:
        print("大一点")
    elif person_number == computer_number:
        print("猜对了")
        break
"""
