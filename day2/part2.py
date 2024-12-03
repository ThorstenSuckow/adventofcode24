
COUNTER = 0

def check_row(row, j) -> bool:
    
    global COUNTER 
    rowlen = len(row)
    safe = True
    res = 0
    idx = -1
        
    j = max(0, min(rowlen-1, j))

    while (j < rowlen -1):
        if ((row[j] - row[j+1] < 0 and res > 0) or 
            (row[j] - row[j+1] > 0 and res < 0)):
            safe = False
            idx = j
            break

        res = row[j] - row[j+1]

        if  res == 0 or abs(res) > 3:
            safe = False
            idx = j
            break

        COUNTER += 1        

        j+=1

    return [safe, idx]                


def process(input: list) -> int:

    global COUNTER
    safe_rows = 0

    for i in range(0, len(input)):
        row = input[i]
        safe = True
           
        [safe, errorIdx] = check_row(row, 0)
        if safe is False:
            
            org = row.copy()
            del row[errorIdx]
            [safe, _] = check_row(row, 0)
            
            row = org.copy()
            del row[errorIdx - 1]
            if safe is False:
                [safe, _] = check_row(row, 0)
            
            row = org.copy()
            del row[errorIdx + 1]
            if safe is False:
                [safe, _] = check_row(row, 0)
            
        if safe is True:
            safe_rows += 1

    return [safe_rows, COUNTER]