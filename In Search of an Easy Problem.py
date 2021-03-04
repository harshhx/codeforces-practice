n = int(input())
survey = list(map(int,input().split()))

if 1 in survey:
	print("HARD")
else:
	print("EASY")