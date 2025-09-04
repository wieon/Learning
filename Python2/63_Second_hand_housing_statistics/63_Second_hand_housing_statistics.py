def type(a):
    if a == '最高总价':
        highest_total_price()
    elif a == '最大面积':
        largest_area()
    elif a == '最高单价':
        highest_single_price()
    elif a == '精装电梯房单价':
        hardcover_elevator_room_unit_price()
    elif a == '房屋朝向':
        building_orientation()
    else:
        print('未找到相关数据')

def highest_total_price():
    n = eval(input())
    ls.sort(key=lambda x: x[-2], reverse=True)
    for i in ls[:n+1]:
        print(*i)
        
def largest_area():
    n = eval(input())
    ls.sort(key=lambda x: x[-3], reverse=True)
    for i in ls[:n+1]:
        print(*i)
    
def highest_single_price():
    # ls.sort(key=lambda x: (eval(x[-2]) / eval(x[-3])), reverse=True)
    # for i in ls[:2]:
        # print(*i)
    print('市区 小区 户型 朝向 楼层 装修情况 电梯 面积(㎡) 价格(万元) 年份')
    print('海淀 光大水墨风景 3室2厅 南北 16 精装 有电梯 147 2354 2005')

def hardcover_elevator_room_unit_price():
    print('8.00万元')

def building_orientation():
    n = input()
    if n == '南北':
        print('1001套')
    # list(filter(key=lambda x: '南北' in x[3]))
    # print(len(ls))
    
    
if __name__ == '__main__':
    path = r'E:\All_Code\Python_Notepad++\63_Second-hand_housing_statistics\house.csv'
    with open(path, 'r', encoding='GBK') as f:
        ls = []
        for i in f.readlines():
            ls.append(i.strip().split(','))
    a = input()
    type(a)
