
def two_sum(array, target):
    result = []
    found_numbers = {}
    for i in array:
        current_value = array[i]
        found_numbers[current_value] = i

        complement = target - current_value
        if complement in found_numbers and found_numbers[complement] != i:
            result.append([i, found_numbers[complement]])
    return result


input_array = [4, 2, 6, 7, 3, 1, 9, 0, 8, 5]
input_target = 10

print two_sum(input_array, input_target)
