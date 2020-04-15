
class BinarySearch:

    def binary_search(self, input_list, first, last, value):
        if first < last:
            mid = int(first+last)//2
            # print(mid)
            if value == input_list[mid]:
                return mid
            elif value < input_list[mid]:
                return self.binary_search(input_list, first, mid, value)
            elif value > input_list[mid]:
                return self.binary_search(input_list, mid+1, last, value)
        else:
            return -1

    def isdupl(self, input_list):
        input_list_len = len(input_list)
        if input_list_len == len(set(input_list)):
            return 0
        else:
            return 1

    def handle_list(self, input_list):
        new_input_list = list(set(input_list))
        return new_input_list


input_list = [1, 4, 5, 6]
value = 6
binary_object = BinarySearch()
if not binary_object.isdupl(input_list):
    first = 0
    last = len(input_list)
    output = binary_object.binary_search(input_list, first, last, value)
    print(output)











# else:
#     first = 0
#     input_list = binary_object.handle_list(input_list)
#     last = len(input_list)-1
#     output = binary_object.binary_search(input_list, first, last, value)
#     print(output)

# first = 0
# last = len(input_list) - 1
# value = 4
# answer = BinarySearchTwo()
# output = answer.binary_search_front(input_list, first, last, value)
# print(output)








