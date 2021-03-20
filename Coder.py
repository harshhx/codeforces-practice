n = int(input())

if n == 1:
	print(1)
	print("C")
else:
	c_count = 0
	ans = []

	for i in range(1,n+1):
		a = []
		for j in range(1,n+1):
			if (i%2 != 0) :
				if j%2 != 0:
					a.append("C")
					c_count += 1
				else:
					a.append(".")
			else:
				if j%2 == 0:
					a.append("C")
					c_count += 1
				else:
					a.append(".") 	
		ans.append(a)


	print(c_count)
	for i in ans:
		for j in i:
			print(j, end="")
		print()
