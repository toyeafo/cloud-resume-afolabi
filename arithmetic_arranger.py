def arithmetic_arranger(numbersList, numbCon):
    if len(numbersList) > 5:
        return "Error: Too Many Problems"
    
    arranged_problems = [[], [], [], []]
    
    for num in numbersList:
        firstNum, operator, secondNum = num.split()
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or'-'."
        
        if not firstNum.isdigit() or not secondNum.isdigit():
            return "Error: Numbers must only contain digits"
        
        if len(firstNum) > 4 and len(secondNum) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        result = calcTwoNum(firstNum, operator, secondNum)
        max_length = max(len(firstNum), len(secondNum), len(str(result)))
        firstNum_display = firstNum.rjust(max_length + 1)
        secondNum_display = operator + secondNum.rjust(max_length)
        seperator_line = "-" * (max_length + 1)
        result_display = str(result).rjust(max_length + 1)
        
        # display_nums = "\n".join([firstNum_display, secondNum_display, seperator_line, result_display])
        arranged_problems[0].append(firstNum_display)
        arranged_problems[1].append(secondNum_display)
        arranged_problems[2].append(seperator_line)
        if numbCon:
            arranged_problems[3].append(result_display)
        
    return "\n".join(["    ".join(row) for row in arranged_problems])
    
def calcTwoNum(firstDigits, operator, secondDigits):
    if (operator =="+"):
        result = int(firstDigits) + int(secondDigits)
    else:
        result = int(firstDigits) - int(secondDigits)
    return result


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))