def print_strings(operation, result): 
    operation = "".join(map(chr, list(map(int, operation))))
    result = "".join(map(chr, list(map(int, result))))

    print(operation)
    print(result)

