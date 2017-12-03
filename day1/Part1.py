def solveCaptcha(inputAsString):
    inputAsIntArray = [int(s) for s in inputAsString]

    result = 0
    if len(inputAsIntArray) <= 1:
        return result

    currentIndex = 0
    for x in inputAsIntArray:
        if currentIndex == (len(inputAsIntArray) - 1):
            next = inputAsIntArray[0]
        else:
            next = inputAsIntArray[currentIndex + 1]

        if x == next:
            result += x
        currentIndex = currentIndex + 1

    return result
