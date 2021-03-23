from fractions import Fraction

m,n = list(map(int,input().split()))

a = max(m,n)
numerator = 6-a+1
denomenator = 6

if numerator%2 == 1:
	if numerator == 3:
		print("1/2")
	else:
		print(f"{numerator}/6")
else:
	if numerator == 4:
		print("2/3")
	else:
		print(f"1/{6//numerator}")