

def narcissistic(value):
    process = [int(i) for i in str(value)]
    power = len(str(value))
    res = 0
    for i in range(power):
        res += process[i] ** power
    if res == value:
        return True
    else:
        return False


print(narcissistic(7))


# test.assert_equals(narcissistic(7), True, '7 is narcissistic');
# test.assert_equals(narcissistic(371), True, '371 is narcissistic');
# test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
# test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')