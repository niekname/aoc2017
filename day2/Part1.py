def calculateChecksum(input):
    result = 0
    for x in input.split('\n'):
        result += calculateSingleRow(x)

    return result


def calculateSingleRow(input):
    arr = [int(s) for s in input.split('\t')]

    smallest = arr[0]
    largest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x

    return largest - smallest
