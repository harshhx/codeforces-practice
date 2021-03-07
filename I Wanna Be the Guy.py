n = int(input())

levels = [i for i in range(1,n+1)]

X_ = list(map(int,input().split()))
X = X_[1:]
Y_ = list(map(int,input().split()))
Y = Y_[1:]

can = list()
for i in range(1,n+1):
	if (i in X) or (i in Y) :
		can.append(i)
if can == levels:
	print("I become the guy.")
else:
	print("Oh, my keyboard!")
