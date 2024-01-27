import re


def calculate(calc: str) -> float:
    """Return the result of a calculation string

    Only support + - * /

    ---
    TODO 
    - add parenthesis
    - support negative numbers (e.g. -1+2)
    - add other operators like exponent, sqrt, etc.
    """
    supported_char = list('0123456789+-*/.')

    for char in calc:
        if char not in supported_char:
            print("Unknown character")
            return 0

    priority = {"*": 1, "/": 1, "+": 2, "-": 2}

    terms  = re.split(r'(\+|\-|\/|\*)', calc)

    for term in terms:
        if term == "":
            print("Invalid Syntax")
            return 0

    if len(terms) <= 1:
        try:
            return float(calc)
        except ValueError:
            print("Invalid Syntax")
            return 0

    # finding the last operation
    max_priority = 0
    last_operator = 0
    for i in range(len(terms)):
        if terms[i] in '+-*/':
            if priority[terms[i]] >= max_priority:
                max_priority = priority[terms[i]]
                last_operator = i
    
    operator = terms[last_operator]
    left_term = calculate(''.join(terms[:last_operator]))
    right_term = calculate(''.join(terms[last_operator+1:]))
    return operation(left_term, right_term, operator)
        


def operation(a: float, b: float, operator: str) -> float:
    result = 0
    match operator:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            try:
                result = a / b
            except ZeroDivisionError:
                print("non")
    return result

def main():
    print(calculate('1.5+2*0.3'))

if __name__ == "__main__":
    main()
