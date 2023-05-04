f = open('26.txt')
n = f.readline()
cubes = sorted([int(i) for i in f], reverse=True)
cklad = []
while len(cubes) > 0:
    block = [cubes.pop(0)]
    for i in range(len(cubes)):
        if (block[-1] - cubes[i]) >= 5:
            block.append(cubes[i])
            cubes[i] = ''
    cklad.append(block)
    cubes = [x for x in cubes if x != '']
print(len(cklad), max(len(c) for c in cklad))
