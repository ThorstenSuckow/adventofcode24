


def process(input: list) -> int:

    sum = 0

    prev = "+"
   
    for i in range(0, len(input)):
        
        el = input[i]

        if el == "+":
            prev = "+"
        if el == "-":
            prev = "-"
        
        if prev == "+" and isinstance(el, list):
            sum += el[0] * el[1]

        if (prev == "-" and isinstance(el, list)):         
            continue        

    return sum