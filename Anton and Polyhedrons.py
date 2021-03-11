n = int(input())
ans = 0

base = {
	"Tetrahedron": 4,
	"Cube": 6,
	"Octahedron": 8,
	"Dodecahedron": 12,
	"Icosahedron" : 20
}

for _ in range(n):
	a = input()
	ans += base[a]
print(ans)