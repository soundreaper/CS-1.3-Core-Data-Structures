#!python

def linear_search(array, item):
    # Time Complexity O(n)

    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index >= len(array):
        return None

    elif array[index] is item:
        return index
    
    return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    # Time Complexity O(log n)

    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)

def middle_calc(low, high):
    return ((low + high) // 2)

def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    low = 0
    high = len(array)
    mid = middle_calc(low, high)

    choice = array[mid]
    
    while not choice == item:
        if choice < item:
            low = mid
        else:
            high = mid
        
        mid = middle_calc(low, high)

        choice = array[mid]
        if low == mid and not choice == item:
            return None
    else:
        return mid
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left is None and right is None:
        left = 0
        right = len(array)
    
    mid = middle_calc(left, right)
    choice = array[mid]

    if choice == item:
        return mid
    else:
        if choice < item:
            left = mid
        else:
            right = mid
        mid = middle_calc(left, right)
        choice = array[mid]

        if left == mid and not choice == item:
            return None

        return binary_search_recursive(array, item, left, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests