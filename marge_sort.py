# complexity o(nlogn)
def recursive_sort(lst):
    """
    Recursive function to sort a list in ascending order.
    Uses the merge sort algorithm.
    """
    # Base case: If the list has only one element or is empty, it is already sorted
    if len(lst) <= 1:
        return lst

    # Divide the list into two halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Recursively sort the two halves
    left_sorted = recursive_sort(left_half)
    right_sorted = recursive_sort(right_half)

    # Merge the sorted halves back together
    merged = merge(left_sorted, right_sorted)

    return merged


def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.
    """
    merged = []
    i = j = 0

    # Compare elements from the two lists and add the smaller element to the merged list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add the remaining elements from either the left or right list
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Example usage:


my_list = [7, 5, 3, 2, 6, 1, 9]
sorted_list = recursive_sort(my_list)
print(sorted_list)  # [1, 2, 3, 5, 6, 7, 9]
