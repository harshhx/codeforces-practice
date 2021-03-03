pos = int(input())
if pos<=5:
	print(1)
elif pos%5 == 0:
	print(pos//5)
else:
	print((pos//5)+1)