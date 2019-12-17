import sys

def calculate_2(token, x, y):
    if token == "*":
        if x == "T" and y == "T":
            return "T"
        else:
            return "F"
    
    if token == "+":
        if x == "F" and y == "F":
            return "F"
        else:
            return "T"
    
        
def circuit_eval(dic, circuit):
    operandStack = []
    circuit_List = circuit.split()
    
    for token in circuit_List:
        if token in dic:
            operandStack.append(dic[token])
            
        else:
            if token == "*" or token == "+":
                operand1 = operandStack.pop()
                operand2 = operandStack.pop()
                result = calculate_2(token, operand1, operand2)
                operandStack.append(result)
            else:
                operand = operandStack.pop()
                if operand == "T":
                    result = "F"
                else:
                    result = "T"
            
                operandStack.append(result)
                
    return operandStack.pop()

def main(data):
    n = int(data.readline().strip())
    
    dic = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    t_string = data.readline().strip()
    t_value = t_string.split(" ")
    for i in range(len(t_value)):
        dic[alphabet[i]] = t_value[i]
    
    
    circuit = data.readline().strip()
    print(circuit_eval(dic, circuit))
    
if __name__ == "__main__":
    main(sys.stdin)