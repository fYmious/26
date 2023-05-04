free_space = int(((open('27886.txt').readlines())[0].split())[0])
data = sorted([int(i) for i in (open('27886.txt').readlines())[1:]])
counter = 0
for count in range(len(data)):
    if counter + data[count] > free_space: break
    counter += data[count]
print(count)
print(data[count] + (free_space - counter) if (data[count] + (free_space - counter)) in data[count:] else '')