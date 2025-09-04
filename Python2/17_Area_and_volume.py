import math


def type_judge(geom_type):
    """接收一个字符串为参数，根据参数判断几何体类型
    若输入为二维图形，计算其面积
    若输入为三维图形，计算其面积与体积
    根据类型调用不同的函数进行运算。
    """
    if geom_type == '长方形':
        length, width = map(float, input().split())  # 空格分隔的输入切分为列表并映射为浮点数
        return square(length, width)                 # 调用函数计算长方形面积
    elif geom_type == '长方体':
        length, width, height = map(float, input().split())  # 空格分隔的输入切分为列表并映射为浮点数
        return cube(length, width, height)                   # 调用函数计算长方体表面积与体积
    elif geom_type == '圆形':
        radius = float(input())  # 输入转为浮点数
        return circle(radius)    # 调用函数计算圆面积
    elif geom_type == '球':
        radius = float(input())  # 输入转为浮点数
        return sphere(radius)    # 调用函数计算球表面积与体积
    elif geom_type == '圆柱体':
        radius, height = map(float, input().split())  # 空格分隔的输入切分为列表并映射为浮点数
        return cylinder(radius, height)  # 调用函数计算圆柱体表面积与体积
    elif geom_type == '圆锥':
        radius, height = map(float, input().split())  # 空格分隔的输入切分为列表并映射为浮点数
        return cone(radius, height)  # 调用函数计算圆锥表面积与体积
    elif geom_type == '正三棱柱':
        side, height = map(float, input().split())
        return tri_prism(side, height)
    else:
        return f'未找到{geom_type}计算方法'


def square(length, width):
    """计算长方形的面积"""
    area_of_square = length * width
    return f'长方形的面积为{area_of_square:.2f}'

def cube(length, width, height):
    """计算长方体的表面积和体积"""
    area_of_cube = length * width * 2 + width * height * 2 + length * height * 2
    volume_of_cube = length * width * height
    return f'长方体的表面积为{area_of_cube:.2f}, 体积为{volume_of_cube:.2f}'

def circle(radius):
    """接收圆的半径，返回圆形的面积，圆周率用math.pi"""
    area_of_circle = math.pi * radius**2
    return f'圆的面积为{area_of_circle:.2f}'

def sphere(radius):
    """接收球的半径，返回球的表面积和体积，圆周率用math.pi"""
    area_of_sphere = 4 * math.pi * radius**2
    volume_of_sphere = 4/3 * math.pi * radius**3
    return f'球的表面积为{area_of_sphere:.2f}, 体积为{volume_of_sphere:.2f}'

def cylinder(radius, height):
    """接收圆柱体的底面半径和高，返回圆柱体的表面积和体积，圆周率用math.pi"""
    area_of_cylinder = 2 * math.pi * radius**2 + 2 * math.pi * radius * height
    volume_of_cylinder = math.pi * radius**2 * height
    return f'圆柱体的表面积为{area_of_cylinder:.2f}, 体积为{volume_of_cylinder:.2f}'

def cone(radius, height):
    """接收圆锥的底面半径和高，返回圆锥的表面积和体积，圆周率用math.pi"""
    area_of_cone = math.pi * radius**2 + math.pi * radius * math.sqrt(height**2+radius**2)
    volume_of_cone = 1/3 * math.pi * radius**2 * height
    return f'圆锥的表面积为{area_of_cone:.2f}, 体积为{volume_of_cone:.2f}'

def tri_prism(side, height):
    """接收正三棱柱的底面边长和高，返回正三棱柱的表面积和体积，圆周率用math.pi"""
    area_of_tri_prism = 3 * side * height + math.sqrt(3)/2 * side**2
    volume_of_tri_prism = math.sqrt(3)/4 * side**2 * height
    return f'正三棱柱的表面积为{area_of_tri_prism:.2f}, 体积为{volume_of_tri_prism:.2f}'


# 参考前面的方法自定义一个函数计算正三棱柱的表面积与体积，
# 函数名为tri_prism()
# 函数接受底边长和高两个参数side, height


if __name__ == '__main__':
    type_of_geometry = input()               # 接收用户输入的字符串
    geometry = type_judge(type_of_geometry)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果