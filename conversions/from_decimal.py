def decimal_to_binary(decimal:int):
    decimal_clone = decimal
    iterations = 0
    multiplier = 1
    binary_value = 0
    values_list = []

    while(decimal_clone != 0):
        decimal_clone = int(decimal_clone / 2)
        iterations += 1
    
    for i in range(0, iterations):
        values_list.append(int(decimal % 2))
        decimal = int(decimal / 2)

    for i in range(0, iterations):
        binary_value += (values_list[i] * multiplier)
        multiplier *= 10

    return binary_value


def decimal_to_octal(decimal:int):
    decimal_clone = decimal
    multiplier = 1
    octal_value = 0

    while(decimal_clone != 0):
        octal_value = int(octal_value + (decimal_clone % 8) * multiplier)
        decimal_clone = int(decimal_clone / 8)
        multiplier *= 10

    return octal_value


def decimal_to_hexadecimal(decimal:int):
    decimal_clone = decimal
    decimal_clone_1 = decimal
    hexadecimal_temp = 0
    iterations = 0
    hexadecimal_value= ''
    hexadecimal_list = []
    hexadecimal_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    while(decimal_clone != 0):
        decimal_clone = int(decimal_clone / 16)
        iterations += 1

    for i in range(0, iterations):
        hexadecimal_temp = int(decimal_clone_1 % 16)
        decimal_clone_1 = int(decimal_clone_1 / 16)
        hexadecimal_list.append(hexadecimal_temp)

    for i in range(0, iterations):
        hexadecimal_value += hexadecimal_map[hexadecimal_list[i]]

    return hexadecimal_value [::-1]
    