import money


# 定义发工资模块，用来增加收入计算
def send_money():
    money.saved_money += 1000
    return money.saved_money
