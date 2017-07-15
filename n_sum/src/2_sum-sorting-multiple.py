
def copy_and_sort(array):
    new_array = list(array)
    new_array.sort()
    return new_array


def two_sum(array, target):
    def find_numbers_on_sorted_array(sorted_array):
        result = []
        i = 0
        j = len(sorted_array) - 1
        while i < j:
            sum = sorted_array[i] + sorted_array[j]
            if sum == target:
                result.append([i, j])
                i += 1
                j -= 1
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1

        return result

    numbers = find_numbers_on_sorted_array(copy_and_sort(array))

    def find_correct_indexes(pair):
        first = -1
        second = -1
        for i in array:
            if array[i] == pair[0]:
                first = i
            if array[i] == pair[1]:
                second = i
            if first != -1 and second != -1:
                return [first, second]

    result = []
    for pair in numbers:
        result.append(find_correct_indexes(pair))
    return result


input_array = [4, 2, 6, 7, 3, 1, 9, 0, 8, 5]
input_target = 10

print two_sum(input_array, input_target)
