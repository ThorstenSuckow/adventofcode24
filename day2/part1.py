


def process(input: list) -> int:

    safe_rows = 0

    for i in range(0, len(input)):
        row = input[i]
        safe = True
        listlen = len(row)
        res = 0
        prev = -1
        for j in range(0, listlen):
            if j+1 < listlen:

                # order changed
                if ((row[j] - row[j+1] < 0 and res > 0) or
                   (row[j] - row[j+1] > 0 and res < 0)):
                    safe = False
                    break

                res = row[j] - row[j+1]
  
                # neither an increase or a decrease
                # Any two adjacent levels differ by at
                #  least one and at most three.
                if  res == 0 or abs(res) > 3:
                    safe = False
                    break
                
        if safe is True:
            safe_rows += 1

    return safe_rows