# 购物车

goods=[
{"name":"电脑","price":4999},
{"name":"鼠标","price":80},
{"name":"游艇","price":200000},
{"name":"别墅","price":2000000},]

money = eval(input())
for i in range(len(goods)):
    print(i, goods[i]["name"])
choice = eval(input())
if goods[choice]["price"] > money:
    print('账户余额不足,先去赚钱吧！')
else:
    print(f'恭喜你成功购买一个{goods[choice]["name"]}')
    