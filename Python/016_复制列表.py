import copy

li = [1,2,3,4]
li2 = copy.copy(li)  # 浅复制，指向原对象
print(li2)
li3 = copy.deepcopy(li)  # 深复制，生成新对象
print(li3)
li4 = li  # 浅复制
print(li4)