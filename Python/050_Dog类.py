class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over.")

my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()


"""
根据类来创建对象称为实例化。
Python中，首字母大写的名称指类（如Dog），小写指根据类创建的实例（如my_dog）。
类中的函数称为方法。
__init__()的下划线旨在避免Python的默认方法与普通方法发生名称冲突。
实参self必不可少，且必须位于其他方法前面。
self.name = name 前一个name为变量，后一个name为形参。
self.name = name获取储存在形参中的值，并将其存储到变量中，然后该变量被关联到当前创建的实例。
可通过实例访问的变量称为属性（如name），而 Willie 为属性的值。
"""
