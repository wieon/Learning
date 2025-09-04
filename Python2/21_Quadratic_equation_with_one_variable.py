import math
a = eval(input())
b= eval(input())
c = eval(input())
if a == 0 and b == 0:
	print("Data error!")
elif a == 0 and b != 0:
	x = -c / b
	print(f'{x:.2f}')
elif a != 0 and b != 0:
	delta = b**2 - 4*a*c
	if delta < 0:
		print('该方程无实数解')
	elif delta == 0:
		x = -b / (2*a)
		print(f'{x:.2f}')
	else:
		x1 = (-b + math.sqrt(delta)) / (2*a)
		x2 = (-b - math.sqrt(delta)) / (2*a)
		print(f"{x1:.2f} {x2:.2f}")