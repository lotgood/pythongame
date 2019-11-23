Lists = []
file = open("1List.txt", "r")
for line in file:
    print(line.strip('\n'))
    Lists.append(line.strip('\n'))
print(Lists)
file.close()
f = open("1list.txt", 'r')
loop_max = (len(f.readlines()))
k = 0
put = input("입력")
for k in range(k, loop_max):
    print(Lists[k])
    print(k)
    if Lists[k] == put:
        print("true")
    k = k + 1
