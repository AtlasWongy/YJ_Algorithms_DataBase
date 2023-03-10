inputIntegers = input('Enter a bunch of random unsorted numbers: ')
inputArray = list(inputIntegers)


def insertion_sort(arr):
    for i in range(1, len(arr), 1):

        sorting_node = arr[i]

        while sorting_node < arr[i - 1] and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1

    return arr


print(f'The sorted array is {insertion_sort(inputArray)}')
