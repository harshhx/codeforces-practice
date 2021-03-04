n = int(input())

friend = [0]

test = list(map(int,input().split()))

friend = friend + test

ans = [0] + [0]*n

for i in range(1,n+1):
	ans[friend[i]] = i

for i in ans[1:]:
	print(i , end = " ")
