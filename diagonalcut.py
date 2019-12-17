# Problem name: Diagonal Cut; Difficulty: 4.8
# This solution is not being accepted on Kattis. Will look at it later

def ptdt(m, n, p3):
    if p3[1] == -m/n * p3[0] + m:
        return True
    return False

count = 0
line = input()
line = line.split(" ")
m = int(line[0])
n = int(line[1])
p1 = [0,m]
p2 = [n,0]

for i in range(n):
    if i < n/2:
        for j in range(m//2, m):
            p3 = [i+0.5, j+0.5]
            if ptdt(m,n, p3):
                count +=1
    else:
        for j in range(0, m//2):
            p3 = [i+0.5, j+0.5]
            if ptdt(m,n, p3):
                count +=1

print(count)
