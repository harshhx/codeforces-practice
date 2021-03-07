n = int(input())
soldiers = list(map(int,input().split()))

tallest = soldiers.index(max(soldiers))+1
smallest = 0
for i in range(len(soldiers)):
	if soldiers[i] == min(soldiers):
		smallest = i
smallest += 1

if smallest - tallest > 0:
	a = tallest -1
	b =  n - smallest
	print(a+b)
else:
	a = tallest -1
	b =  n - smallest
	print(a+b-1)
