
def two_sum(array, target):
    found_numbers = {}
    for i in array:
        current_value = array[i]
        found_numbers[current_value] = i

        complement = target - current_value
        if complement in found_numbers:
            return [i, found_numbers[complement]]

    raise Exception("problem without solution")


input_array = [4, 2, 6, 7, 3, 1, 9, 0, 8, 5]
input_target = 16

print two_sum(input_array, input_target)
