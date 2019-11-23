score = 0
Lists = []
file = open("1List.txt", "r")
for line in file:
    Lists.append(line.strip('\n'))
print(Lists)
file.close()
f = open("1list.txt", 'r')
loop_max = (len(f.readlines()))
k = 0
while True:
    put = input("아는 인물을 입력해주세요")
    for k in range(k, loop_max):
        if Lists[k] == put:
            print("맞추셨습니다 점수:")
            score = score + 1
            print(score)
            k = k + 1
        if k == loop_max:
            break
