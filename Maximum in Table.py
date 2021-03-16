n = int(input())

table = [[1]*n]*n
cur = 1


for i in range(1,n):
	for j in range(1,n):
		table[i][j] = table[i-1][j] + table[i][j-1]
		x = table[i][j] 
		cur = max(cur,x)
print(cur)

