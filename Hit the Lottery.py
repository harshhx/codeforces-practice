n = int(input())

ans = 0

while n>0:
	if n%100 == 0:
		ans += n//100
		n = n%