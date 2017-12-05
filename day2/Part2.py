def calculateChecksum(input):
    result = 0
    for x in input.split('\n'):
        result += calculateSingleRow(x)

    return result


def calculateSingleRow(input):
    arr = [int(s) for s in input.split('\t')]

    result = 0
    for x in arr:
        for y in arr:
            if x == y:
                continue
            elif x % y == 0:
                result += x / y

    return result
