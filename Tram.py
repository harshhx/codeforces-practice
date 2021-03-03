n = int(input())
inc = []
out = []
for _ in range(n):
	test = list(map(int,input().split()))
	out.append(test[0])
	inc.append(test[1])
currPas = 0
cap = 0

for i in range(n):
	currPas = currPas - out[i]
	currPas = currPas + inc[i]
	cap = max(currPas,cap)
print(cap)