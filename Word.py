s = input()

UC = 0
LC = 0

for i in s:
	if i.isupper():
		UC += 1
	else:
		LC += 1
if UC>LC:
	print(s.upper())
else:
	print(s.lower())