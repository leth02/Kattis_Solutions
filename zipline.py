# Problem name: Zipline; Difficulty: 3.6

import sys

def pytago(a, b):
    answer = (a**2 + b**2)**0.5
    return answer
    
    
def main(data):
    n = int(data.readline().strip())  
    answer = ""
    for i in range(n):
        l = data.readline().strip()
        line = l.split(" ")
        w = int(line[0])
        g = int(line[1])
        h = int(line[2])
        r = int(line[3])

        min_value = pytago((h-g), w)
        if g == h and g == r:
            max_value = min_value
        else:
            max_value = pytago((w * ((h-r)/(g+h-2*r))), (h-r)) + pytago((w*((g-r)/(g+h-2*r))), (g-r))
        answer += str(min_value) + " "
        answer += str(max_value) + "\n"
    print(answer)

if __name__ == "__main__":
    main(sys.stdin)