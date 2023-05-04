free_space = int(((open('27885.txt', 'r').readlines())[0].split(' '))[0])
data = sorted([int(i) for i in (open('27885.txt', 'r').readlines())[1:]])
counter = 0
for count in range(len(data)):
    if counter + data[count] > free_space: break
    counter += data[count]
print(count)
print((zapas + data[count]) if ((zapas := free_space - counter) + data[count]) in data[count:] else 'vlad marmelad')