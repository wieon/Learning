def calc(a, b):
	return a+b

print(calc(10, 20))

s = lambda a,b:a+b
print(type(s))
print(s(1,2))

print('-'*30)

ls = ['1', '2', '3', '4']
for i in ls:
	print(i)
for i in range(len(ls)):
	print(ls[i])