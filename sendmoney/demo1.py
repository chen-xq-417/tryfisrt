"""
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额

"""
# 原有存款1000元
saved_money = 1000


# 定义发工资模块，用来增加收入计算
def send_money():
    global saved_money
    saved_money += 1000
    return saved_money


# 定义工资查询模块，用来展示工资数额
def select_money():
    print(send_money())


# 定义一个启动文件，展示最终存款
if __name__ == '__main__':
    select_money()
