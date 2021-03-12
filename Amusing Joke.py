host = input()
guest = input()
pile = input()


a = list(host+guest)
a = a.sort()
pile = list(pile).sort()

if a == pile:
	print("YES")
else:
	print("NO")


"""map_ = {}

for i in host:
	if i in map_:
		map_[i] += 1
	else:
		map_[i] = 1

for i in guest:
	if i in map_:
		map_[i] += 1
	else:
		map_[i] = 1

for i in pile:
	if i in map_:
		map_[i] -= 1
	else:
		map_[i] = 1

x = map_.values()

if 1 in x or -1 in x:
	print("NO")
else:
	print("YES")"""