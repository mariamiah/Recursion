list2 = [1, 2, [3, 4]]


def sum_list(list2):
    if not isinstance(list2, list):
        return list2
    sum = 0
    for number in list2:
        sum += sum_list(number)
    return sum

print(sum_list(list2))

