def selection_sort(arr):
    n = len(arr)

    for pass_num in range(n - 1):
        min_index = pass_num

        for i in range(pass_num + 1, n):
            if arr[i] < arr[min_index]:
                min_index = i
        temp = arr[pass_num]
        arr[pass_num] = arr[min_index]
        arr[min_index] = temp

# Example usage:
T = [5, 2, 9, 1, 5, 6]
selection_sort(T)
print("Sorted array:", T)
