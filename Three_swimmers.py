def time_to_wait_a(p,a):
	if p % a == 0:
		return 0
	pf = p//a
	return ((pf+1)*a - p)

def time_to_wait_b(p,b):
	if p % b == 0:
		return 0
	pf = p//b
	return ((pf+1)*b - p)

def time_to_wait_c(p,c):
	if p % c == 0:
		return 0
	pf = p//c
	return ((pf+1)*c - p)

def time_to_wait(p,a,b,c):
	return(min(time_to_wait_a(p,a),time_to_wait_b(p,b),time_to_wait_c(p,c)))

t = int(input())

for _ in range(t):
	test = list(map(int,input().split()))
	print(time_to_wait(test[0],test[1],test[2],test[3]))


