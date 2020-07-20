""" insertion sort written by Matt during lecture """
def insertion_sort(input_list):
    # think of the first element as sorted

    # for all unsorted items
    for i in range(1, len(input_list)):
        # mark the current item we are considering
        current = input_list[i]

        # look left until we find the proper
        # place to insert the current item
        j = i
        while j > 0 and current < input_list[j-1]:
            # as we are "looking left", we need to
            # shift items to the right
            input_list[j] = input_list[j-1]
            j -= 1

        # when we've found our insertion point (j)
        # insert item
        input_list[j] = current

    return input_list


# Own work below:

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # find the smallest item in arr[i:]
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap to put the smallest item found in its place
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

def bubble_sort(arr):
    # control boolean
    swapped = True
    while swapped:  # while we have swapped something...
        swapped = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                # elements are out of place, swap them
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
