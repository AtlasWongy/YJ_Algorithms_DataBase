randomArray = [3, 2, 5, 7, 4]
#randArray2 = 84357438

inputIntegers = input('Enter a bunch of random unsorted numbers: ')
inputArray = list(inputIntegers)

def insertion_sort(arr):


    for i in range(1, len(arr), 1):

        sortingNode = arr[i]

        while sortingNode < arr[i - 1] and i > 0 :

            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1
    
    return arr

print(insertion_sort(inputArray))

