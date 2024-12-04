


def process(input: list) -> int:

    sum = 0

    for i in range(0, len(input)):
        
        sum += input[i][0] * input[i][1]
        
    return sum