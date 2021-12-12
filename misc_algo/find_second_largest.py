inputData = input("Enter an array of integers: ")
inputDataList = list(inputData)

# Sort the list first. Using quick_sort here
# Drop all duplicates
# Find the largest integer and drop it
# Find the next largest integer and drop it

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    else:

        pivot = arr.pop()

        arrBig = []
        arrSmall = []

        for i in range(0, len(arr), 1):

            if pivot > arr[i]:
                arrSmall.append(arr[i])
            else:
                arrBig.append(arr[i])
        
        return quick_sort(arrSmall) + [pivot] + quick_sort(arrBig)


def find_second_largest(arr):

    # Remove duplicates first

    removeDuplicates = set(arr)
    updatedArray = list(removeDuplicates)

    sortedArray = quick_sort(updatedArray)

    print(f"The sorted array with removed duplicates is {sortedArray}")
    sortedArray.pop()
    secondLargest = sortedArray.pop()

    print(f"The second largest integers is {secondLargest} ")
    return secondLargest

print(find_second_largest(inputDataList))