import random

# 1. binary search

array_of_randoms = sorted([random.randint(1, 1000) for a in range(100)])
array_of_randoms = set(array_of_randoms)
array_of_randoms = sorted(list(array_of_randoms))


# Return the index of the the found number or -1 if it is not found
# complexity o(logn)
def binary_search(array, number_to_find):
    left = 0
    right = len(array)-1
    count = 0
    while left <= right:
        count += 1
        mid = (left+right)//2
        #print(left, right, mid)
        if array[mid] == number_to_find:
            return mid, count
        else:
            if number_to_find < array[mid]:
                right = mid-1
            else:
                left = mid+1
    return count


def binary_search_test():
    print(array_of_randoms)

    count_test = 0
    count_interaction = 0

    for i in range(99):

        random_array_index = random.randint(0, len(array_of_randoms)-1)

        number_to_find = array_of_randoms[random_array_index]

        found_index = binary_search(array_of_randoms, number_to_find)

        count_interaction += found_index[1]

        count_test += 1


        print(f'num_to_find= {number_to_find}, {found_index}, {random_array_index}')

        #רשימה של מספר איטרציות בכל חיפוש


    not_found_index = binary_search(array_of_randoms, 9999999)

    print("When not found should be -1", not_found_index)

    average = count_interaction / count_test
    print(f'The average of the number of iterations for the searches made is: {average}')

binary_search_test()


