def bubble_sort(arr):
    n = len(arr)
    
    for pass_num in range(n - 1):
        for i in range(n - 1, pass_num, -1):
            if arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp

# Example usage:
T = [5, 2, 9, 1, 5, 6]
bubble_sort(T)
print("Sorted array:", T)