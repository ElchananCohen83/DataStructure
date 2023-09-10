import random

array_of_randoms = sorted([random.randint(1, 1000) for a in range(100)])
print(array_of_randoms)

# Return the index of the found number or -1 if it is not found

# complexity o(logn)


def binary_search(array, number_to_find):

    return binary_search_recursive(array, number_to_find, 0, len(array)-1)


def binary_search_recursive(array, number_to_find, start_index, end_index):
    count = 0
    if len(array) == 0:
        return 'list is empty'
    elif len(array) == 1:
        if array[0] == number_to_find:
            return f'number: {number_to_find} in index: 0'
        else:
            return f'The number {number_to_find} does not exist in the list'
    while start_index <= end_index:
        count += 1
        mid = (start_index + end_index) // 2
        print(array[mid], number_to_find, mid, start_index, end_index)
        if array[mid] == number_to_find:
            return [f'The number: {number_to_find}, you were looking for is in the array at index: {mid}.', count]
        else:
            if array[mid] > number_to_find:
                return binary_search_recursive(array, number_to_find, start_index, mid-1)
            else:
                return binary_search_recursive(array, number_to_find, mid+1, end_index)
    return [f'The number {number_to_find} does not exist in the list', count]


# found_number = binary_search(array_of_randoms, 11)

# print(found_number)

def binary_search_test():

    count_test = 0
    count_interaction = 0

    for i in range(99):

        random_array_index = random.randint(0, len(array_of_randoms)-1)

        number_to_find = array_of_randoms[random_array_index]

        found_index = binary_search_recursive(array_of_randoms, number_to_find, start_index=0, end_index=len(array_of_randoms)-1)

        count_interaction += found_index[1]

        count_test += 1


        print(f'num_to_find= {number_to_find}, {found_index}, {random_array_index}')

        #רשימה של מספר איטרציות בכל חיפוש


    not_found_index = binary_search(array_of_randoms, 9999999)

    print("When not found should be -1", not_found_index)

    average = count_interaction / count_test
    print(f'The average of the number of iterations for the searches made is:{count_interaction}/{count_test}= {average}')

binary_search_test()
