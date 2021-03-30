n,k = list(map(int,input().split()))

arr = []
if n%2 == 0:
	for i in range(1,n,2):
		arr.append(i)
	for i in range(2,n+1,2):
		arr.append(i)
else:
	for i in range(1,n+1,2):
		arr.append(i)
	for i in range(2,n,2):
		arr.append(i)
print(arr[k-1])
