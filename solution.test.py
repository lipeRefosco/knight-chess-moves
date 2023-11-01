from solution import solution

def test_one():
    given_src = 19
    given_dest = 36

    expected = 1

    result = solution(given_src, given_dest)
    return (expected == result, (given_src, given_dest), expected, result)

def test_two():
    given_src = 0
    given_dest = 1

    expected = 3

    result = solution(given_src, given_dest)
    return (expected == result, (given_src, given_dest), expected, result)


print(test_one())
print()
print()
print()
print(test_two())
