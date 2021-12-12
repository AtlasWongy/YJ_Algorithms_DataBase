intervalOne = [ [1, 3], [5, 7], [2, 4], [6, 8] ]
intervalTwo = [ [1, 3], [7, 9], [4, 6], [10, 13] ]

# sort the list by increasing order with regards to the left timing
# Example: [1, 3] then [2, 4] then [5, 7]
# Use any sorting algorithms
# Using insertion sort in this example

def insertion_sort(arr):

    for i in range(1, len(arr), 1):

        sortingNode = arr[i]

        while sortingNode < arr[i - 1] and i > 0 :

            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1
    
    return arr

def checkInterval(arr):

    arrInput = insertion_sort(arr)

    for i in range(0, len(arrInput) - 1, 1):

        if arrInput[i][1] > arrInput[i + 1][0]:

            print("There seems to an interval overlap")
            return False

    print("No overlap found")
    return True

print(checkInterval(intervalOne))
print(checkInterval(intervalTwo))