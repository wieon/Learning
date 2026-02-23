# 在列表后加"END"
# None为不变对象，多任务环境下同时读取对象不需要加锁，不会报错
# 如果写成L=[]，[]为可变对象，多次调用函数时参数改变

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L