test = list(map(int,input().split()))
n,h = test

height = list(map(int,input().split()))

width = 0

for i in height:
	if i>h:
		width += 2
	else:
		width += 1

print(width)
