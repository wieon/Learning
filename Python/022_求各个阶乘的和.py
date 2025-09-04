# 求1+2!+3!+...+20!的和

sum = 0
factorial = 1
for n in range(1, 21):
	factorial *= n
	sum += factorial
print(sum)