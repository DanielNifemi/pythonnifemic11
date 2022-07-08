def two_sum(list_of_numbers, target):
    """
    Given a list of numbers and a target number, return  list of all pairs of
    indices that add up to the target"""
    result = []
    for i in range(len(list_of_numbers)):
        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[i] + list_of_numbers[j] == target:
                result.append((i, j))
    return result


print(two_sum([3, 1, 5, -8], 6))
print(two_sum([3, 3], 6))
print(two_sum([3, 3, 3], 6))

