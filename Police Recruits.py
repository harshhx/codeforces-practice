n = int(input())
a = list(map(int,input().split()))
cur = 0
untreated = 0
for i in a:
	if i == -1 and cur == 0:
		untreated += 1
	elif i == -1 and cur>0:
		cur -= 1
	else:
		cur += i
print(untreated)
