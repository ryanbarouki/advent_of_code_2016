lines = []

with open('input.txt') as f:
	line = f.readline()
	while line:
		line = line.split()
		lines.append(line)
		line = f.readline()

def isTriangle(triangle):
	a = int(triangle[0])
	b = int(triangle[1])
	c = int(triangle[2])
	return (a + b > c) and (a + c > b) and (b + c > a)

def getTriangles(array):
    triangles = []
    for i in range(0, len(array), 3):
        for j in range(0, 3):
            triangles.append([array[i][j], array[i+1][j], array[i+2][j]])

    return triangles

numTriangles = len([x for x in lines if isTriangle(x)])
numTrianglesPart2 = len([x for x in getTriangles(lines) if isTriangle(x)])

print("Number of triangles: {}".format(numTriangles))
print("Number of triangles part 2: {}".format(numTrianglesPart2))