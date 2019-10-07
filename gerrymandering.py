# Problem name: Gerrymandering; Difficulty: 1.4

line = input()
line = line.split(" ")
P = int(line[0])
D = int(line[1])
district = {}
total = 0
waste_A = 0
waste_B = 0
answer = ""
for i in range(P):
    line = input()
    line = line.split(" ")
    distr = line[0]
    A_vote = int(line[1])
    B_vote = int(line[2])
    district[distr] = district.get(distr, [0, 0])
    district[distr][0] += A_vote
    district[distr][1] += B_vote

for i in range(D):

    temp = district[str(i+1)]
    
    if temp[0] > temp[1]:
        waste = 0
        answer += "A "
        waste = temp[0] - ((temp[0] + temp[1])//2 + 1)
        waste_A += waste
        answer += str(waste) + " "
        waste_B += temp[1]
        answer += str(temp[1])
        
    
    else:
        waste = 0
        answer += "B "
        waste = temp[1] - ((temp[0] + temp[1])//2 + 1)
        waste_B += waste
        answer += str(temp[0]) + " "
        answer += str(waste)
        waste_A += temp[0]

    answer += "\n"
    total += temp[0] + temp[1]

E = abs(waste_A - waste_B) / total
print(answer, end = "")
print("%.10f" %E)


