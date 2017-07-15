
def copy_and_sort(array):
    new_array = list(array)
    new_array.sort()
    return new_array


def two_sum(array, target):
    def find_numbers_on_sorted_array(sorted_array):
        i = 0
        j = len(sorted_array) - 1
        while i < j:
            sum = sorted_array[i] + sorted_array[j]
            if sum == target:
                return [i, j]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1

        raise Exception("problem without solution")

    numbers = find_numbers_on_sorted_array(copy_and_sort(array))

    first = -1
    second = -1
    for i in array:
        if array[i] == numbers[0]:
            first = i
        if array[i] == numbers[1]:
            second = i
        if first != -1 and second != -1:
            return [first, second]


input_array = [4, 2, 6, 7, 3, 1, 9, 0, 8, 5]
input_target = 16

print two_sum(input_array, input_target)
