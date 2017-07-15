
def binary_search(array, target):
    def loop(start, end):
        if end - start == 1:
            if array[end] == target:
                return end
            elif array[start] == target:
                return start
            else:
                return -1

        mid = start + ((end - start) / 2)
        value = array[mid]
        if value == target:
            return mid
        elif value < target:
            return loop(mid, end)
        elif value > target:
            return loop(start, mid)

    return loop(0, len(array) - 1)


test = [1, 2, 3]
print binary_search(test, 2)
print binary_search(test, 1)
print binary_search(test, 3)