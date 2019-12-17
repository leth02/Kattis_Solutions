import sys

def main(data):
    ip = data.readline().strip()
    
    lst = ip.split(" ")
    swather = int(lst[0])
    stage = int(lst[1])
    
    table1 = [[0 for j in range(stage)] for i in range(swather)]    
    table2 = [[0 for j in range(stage)] for i in range(swather)]
        
    for i in range(swather):
        line = data.readline().strip()
        lst = line.split(" ")
        for j in range(stage):
            table1[i][j] = int(lst[j])
            
        
    table2[0][0] = table1[0][0]
    
    for i in range(1,stage):
        table2[0][i] = table2[0][i-1] + table1[0][i]
    
    for i in range(1, swather):
        table2[i][0] = table2[i-1][0] + table1[i][0]
        
        for j in range(1, stage):
            table2[i][j] = table1[i][j] + max(table2[i-1][j], table2[i][j-1])
    
    
    result = ""
    for num in range(swather):
        result += str(table2[num][stage-1]) + " "
    
    result = result[:-1]
    
    print(result)
    
    
if __name__ == "__main__":
    main(sys.stdin)