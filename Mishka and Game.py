n = int(input())

chris = 0
mishka = 0

for _ in range(n):
	m, c = list(map(int,input().split()))
	if m>c:
		mishka+= 1
	if m<c:
		chris += 1
if mishka>chris:
	print("Mishka")
elif mishka<chris:
	print("Chris")
else:
	print("Friendship is magic!^^")