#/usr/bin/env python3
import sys

def main(data):
    
    N = int(data.readline().strip())
    lst = []
    
    for i in range(N):
        lst.append(data.readline().strip())
        
    count = 1
    result = 0
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == "O":
            result = result + 2**(count-1)
        count += 1
    print(result)
if __name__ == "__main__":
    main(sys.stdin)