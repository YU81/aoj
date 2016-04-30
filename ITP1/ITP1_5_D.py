# coding : utf-8
def include_3(number, counter, lst):
    """
    :param int number:
    :param int ounter:
    :param list[int]lst:
    :rtype: bool
    """
    if (number % 10 == 3):
        lst.append(counter)
        return True
    return False


n = int(input())
counter = 1
result = []
while counter <= n:
    x = counter
    if (x % 3 == 0):
        result.append(counter)
        counter += 1
        continue
    if (include_3(x, counter, result)):
        counter += 1
        continue
    x //= 10
    while x:
        if (include_3(x, counter, result)):
            break
        x //= 10

    counter += 1

print(" " + " ".join([str(x) for x in result]))
