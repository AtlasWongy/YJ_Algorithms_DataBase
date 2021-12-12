
inputData = input("Enter a string to determine if it is a palindrome: ")

def checkIfPalindrome(input):

    inputIntoArray = list(input)

    for i in range(0, len(inputIntoArray) - 1, 1):

        if inputIntoArray[i] == inputIntoArray[(len(inputIntoArray) - 1) - i]:
            print("Seems to be a match")
        else:
            print("The input does not seem to be a palindrome")
            return False

    print("The input is a palindrome")
    return True

print(checkIfPalindrome(inputData))