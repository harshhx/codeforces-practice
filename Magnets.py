n = int(input())

magnets = ""
for _ in range(n):
	magnets += input()

groups = magnets.count("11") + magnets.count("00") + 1

print(groups)