num = eval(input())
text = "Hello World"
if num == 0:
	print(text)
elif num > 0:
    for i in range(0, 11, 2):
        print(text[i:i+2])
else:
	for i in range(len(text)):
		print(text[i])