def prime_or_not(n):
	if n <= 1:
		print(n, "is not a prime.")
	else:
		for i in range(2, int(n/2)+1):
			if n%i == 0:
				print(n, "is not a prime.")
				break
		else:
			print(n, "is a prime.")
			
prime_or_not()