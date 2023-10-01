def merge_sort(arr):
    print('Dividing :', arr)
    
    if len(arr) > 1:
        mid_point = len(arr) // 2
        left_half = arr[:mid_point]
        right_half = arr[mid_point:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    print("Merging :", arr)


if __name__ == '__main__':
    arr = [45, 7, 85, 24, 60, 255, 38, 63, 1]
    merge_sort(arr)
    print('Sorted Array :', arr)
