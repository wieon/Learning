n = eval(input())
sum = 0
if n%2 == 0:
	k = n/2
	for i in range(1,int(k)+1):
		sum += 1/(2*i)
else:
	k = (n+1)/2
	for i in range(1,int(k)+1):
		sum += 1/(2*i-1)
print(f'{sum:.2f}')
