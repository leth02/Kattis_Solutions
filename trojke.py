#/usr/bin/env python3
from operator import itemgetter
import sys

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def trojke(x,y,z):
    lst = [x,y,z]
    
    lst = sorted(lst,key = itemgetter(0,1))
    
    xdif1 = lst[1][0] - lst[0][0]
    ydif1 = lst[1][1] - lst[0][1]
    
    xdif2 = lst[2][0] - lst[1][0]
    ydif2 = lst[2][1] - lst[1][1]
    
    gcd1 = gcd(xdif1,ydif1)
    gcd2 = gcd(xdif2,ydif2)
    
    xdif1 /= gcd1
    ydif1 /= gcd1
    
    xdif2 /= gcd2
    ydif2 /= gcd2
    
    return xdif1 == xdif2 and ydif1 == ydif2
    
def main(data):
    lst = []
    inp = int(data.readline().strip())
    for i in range(inp):
        line = data.readline().strip()
        for j in range(len(line)):
            if line[j] != '.':
                lst.append((i,j))
    
    num = len(lst)
    counter = 0
    for i in range(num):
        for j in range(i+1,num):
            for k in range(j+1, num):
                if trojke(lst[i],lst[j],lst[k]):
                    counter += 1
    print(counter)
    
    
if __name__ == "__main__":
    main(sys.stdin)