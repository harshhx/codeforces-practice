def gcd(a,b):
	if a == 0:
		return b
	if b == 0:
		return a	
	return gcd(b,a%b)

def find_gcd(arr):
	ans = arr[0]
	for i in arr[1:]:
		ans = gcd(ans,i) % 1000000007
	return ans

test = list(map(int,input().split()))
n,q = test

arr = list(map(int,input().split()))



for _ in range(q):
	samp = list(map(int,input().split()))
	i,a = samp
	arr[i-1] = arr[i-1]*a
	print(find_gcd(arr))