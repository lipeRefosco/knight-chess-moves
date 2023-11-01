from utils import sort_by_less_difference

def test_sort_by_less_difference():
    given_list = [13, 45, 23, 60]
    given_sub = 40

    expected = [45, 23,  60, 13]

    result = sorted(given_list, key=lambda x: abs(given_sub - x))
    return (expected == result, (given_list, given_sub), expected, result)

def test_sort_by_less_difference_with_zero_difference():
    given_list = [13, 45, 23, 40, 60]
    given_sub = 40

    expected = [40, 45, 23,  60, 13]

    result = sorted(given_list, key=lambda x: abs(given_sub - x))
    return (expected == result, (given_list, given_sub), expected, result)

print(test_sort_by_less_difference())
print(test_sort_by_less_difference_with_zero_difference())