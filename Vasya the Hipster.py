test = list(map(int,input().split()))
a,b = test
x = max(a,b) - min(a,b)
print(f'{min(a,b)} {x//2}')