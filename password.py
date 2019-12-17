import sys

def main(data):
    lst = []
    
    n = int(data.readline().strip())
    times = 0
    
    for i in range(n):
        line = data.readline().strip()
        password = line.split(" ")
        lst.append(float(password[1]))
    lst.sort(reverse = True)    
    for i in range(n-1, -1, -1):
        times = times + float((i+1)*(lst[i]))
    
    print(times)
    
if __name__ == "__main__":
    main(sys.stdin)