sampleArray = [0, 9, 3, 8, 2, 7, 5]

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        
        arrSmall = []
        arrBig = []

        for items in arr:

            if pivot > items:
                arrSmall.append(items)
            elif pivot < items:
                arrBig.append(items)
        
        return quick_sort(arrSmall) + [pivot] + quick_sort(arrBig)

print(quick_sort(sampleArray))
