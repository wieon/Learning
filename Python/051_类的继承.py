class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size  # 可选的

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self, car_model):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = car_model + " can go approximately " + str(range) + " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类属性，再初始化电动汽车特有属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():  # 重写父类
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
    

my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range("Tesla")


"""
创建子类时，父类必须在当前文件中，且位于子类之前。
定义子类时，必须在括号内指定父类名称。
父类也称为超类，super因此得名。super()将父类和子类关联，调用父类的__init__()方法。

"""