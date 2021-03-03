mat = []
for _ in range(5):
	a = list(map(int,input().split()))
	mat.append(a)

for i in range(5):
    if 1 in mat[i]:
        ind = [i,mat[i].index(1)]
        break
ans = abs(ind[0]-2) + abs(ind[1]-2)
print(ans)