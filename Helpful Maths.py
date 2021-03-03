s = input()
test = list(map(int,s.split("+")))
test.sort()
ans = ""
for i in test:
	ans += str(i)
	ans += "+"
print(ans[:-1])