# Problem name: Missing Number; Difficulty: 1.5

n = int(input())
num = 0
good = True
missing = []
index = 1
for i in range(n):
    num = int(input())
    if num != index:
        good = False
        for j in range(index,num):
            missing.append(j)
        index = num + 1
    else:
        index +=1

if good:
    print("good job")
else:
    for num in missing:
        print(num)