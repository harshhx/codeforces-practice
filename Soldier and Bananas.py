a = list(map(int,input().split()))
k,n,w = a

total_cost = (k*w*(w+1))//2

if total_cost<n:
	print(0)
else:
	print(total_cost-n)
