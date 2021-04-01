while True:
	try:
		a = input()
		if a:
			print("NO")
		else:
			break
	
	except EOFError as e:
		break
	