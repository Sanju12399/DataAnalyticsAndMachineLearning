def bubbleSort(arr):
    n = len(arr)
    # Optimize the code: If the array is already sorted, no need to go through the entire process
    for i in range(n-1):
        # Traverse through all array elements
        # Last i elements are already in place
        swapped = False
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            # If we haven't needed to make a single swap, we can exit the main loop
            return

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
