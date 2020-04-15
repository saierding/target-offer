def sqrt(input_value):
    if input_value <= 3 & input_value > 0:
        return 1
    elif input_value <= 5 & input_value > 3:
        return 2
    elif input_value == 0:
        return 0
    else:
        value = input_value//2
        for i in range(value+1):
            # print(i)
            value_pow = i*i
            if input_value == value_pow:
                return i
            elif input_value < value_pow:
                return i-1

            
output = sqrt(14354543543242)
print(output)