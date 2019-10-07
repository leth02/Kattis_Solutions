# Problem name: Summer Trip; Difficulty: 2.7

import sys

def main(data):
    line = data.readline().strip()
    
    count = 0
    lst = []
    for i in range(len(line)):
        first = line[i]
        lst.append(first)
        
        for j in range(i+1, len(line)):
            last = line[j]
            
            if last not in lst:
                count += 1
                lst.append(last)
            if first == last:
                break
            
        lst = []
             
    print(count)
        
if __name__ == "__main__":
    main(sys.stdin)
    
    
