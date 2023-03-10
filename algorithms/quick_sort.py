inputIntegers = input('Enter a bunch of random unsorted numbers: ')
inputArray = list(inputIntegers)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

        arr_small = []
        arr_big = []

        for items in arr:

            if pivot > items:
                arr_small.append(items)
            elif pivot < items:
                arr_big.append(items)

        return quick_sort(arr_small) + [pivot] + quick_sort(arr_big)


print(f'The sorted array is {quick_sort(inputArray)}')
