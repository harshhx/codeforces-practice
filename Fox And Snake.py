n,m =  list(map(int,input().split()))
snake = []
for _ in range(n):
	cur = ""
	for _ in range(m):
		cur += "."
	snake.append(cur)

at_end = True
for i in range(n):
	if i%2 == 0:
		snake[i] = "#"*m
	else:
		if at_end:
			test = list(snake[i])
			test[-1] = "#"
			a = "".join(test)
			snake[i] = a
			at_end = False
		else:
			test = list(snake[i])
			test[0] = "#"
			a = "".join(test)
			snake[i] = a
			at_end = True

for i in snake:
	print(i)