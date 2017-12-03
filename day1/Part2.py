def solveCaptcha(inputAsString):
    inputAsIntArray = [int(s) for s in inputAsString]

    firstHalf = inputAsIntArray[:len(inputAsIntArray) // 2]
    secondHalf = inputAsIntArray[len(inputAsIntArray) // 2:]
    result = 0

    for x, y in zip(firstHalf, secondHalf):
        if x == y:
            result += x
            result += y

    return result
