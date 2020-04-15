input_list = [5, 1, 2, 3, 0, 4]


def answer(input):
    input_length = len(input)
    output_list = [-1] * input_length

    # for i in range(input_length):
    #     output_list.append(-1)

    for i in range(input_length):
        for j in range(i + 1, input_length):
            if input[i] < input[j]:
                output_list[i] = j
                break
                
    return output_list


print(answer(input_list))