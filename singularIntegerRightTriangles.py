max = 1000
x = 2
triangles =[]
while x <= max:
    if x%12 == 0 or x%30 == 0 or x%40 == 0:
        triangles.append(x)
    x += 2
print(len(triangles))

for triangle in triangles:
    if triangle%12==0 and triangle%30==0 or triangle%30==0 and triangle%40==0 or triangle%12==0 and triangle%40==0:
        triangles.remove(triangle)
print(triangles)
print(len(triangles))