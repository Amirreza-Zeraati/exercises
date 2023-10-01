def binary_search(array, x):
    first = 0
    last = len(array) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if array[mid_point] == x:
            return True
        else:
            if x < array[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return False


def binary_search_recursive(array, first, last, x):
    # in recursive, the array have to be sorted first
    # you can also use merge sort in my < exercises > repo
    array.sort()
    if len(array) == 0:
        return False
    else:
        if last == first:
            return False
        mid_point = (first + last) // 2
        if array[mid_point] == x:
            return True
        else:
            if x < array[mid_point]:

                last = mid_point - 1
                return binary_search_recursive(array, first, last, x)
            else:
                first = mid_point + 1
                return binary_search_recursive(array, first, last, x)


if __name__ == '__main__':
    array = [102, 4, 7, 1, 19, 14, 28, 211, 3, 32]
    print('Binary Search : ', binary_search(array, 61)) # False
    print('Binary Search Recursive : ', binary_search_recursive(array, 0, len(array) - 1, 4)) # True
