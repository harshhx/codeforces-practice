n = input()
test = list(str(n))

if (test.count("4") + test.count("7") == 4) or (test.count("4") + test.count("7") == 7):
	print("YES")
else:
	print("NO")