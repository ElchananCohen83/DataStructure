def quick_sort(arr):
    # Base case: If the list has only one element or is empty, it is already sorted
    if len(arr) <= 1:
        return arr

    # Select the pivot element (in this case, the first element)
    pivot = arr[0]

    # Create two empty lists to store elements smaller and greater than the pivot
    smaller = []
    greater = []

    # Partition the list into two sublists based on the pivot
    for element in arr[1:]:
        if element < pivot:
            smaller.append(element)
        else:
            greater.append(element)

    # Recursively call quicksort on the sublists, then concatenate the sorted sublists
    return quick_sort(smaller) + [pivot] + quick_sort(greater)

# Example usage


my_list = [5, 2, 9, 1, 7, 6, 3]
sorted_list = quick_sort(my_list)
print(sorted_list)
