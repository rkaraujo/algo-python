# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
    majority_even = is_majority_even(integers)
    if majority_even:
        return next((num for num in integers if not is_even(num)))
    else:
        return next((num for num in integers if is_even(num)))


def is_majority_even(integers):
    first3 = integers[:3]
    return (is_even(first3[0]) and is_even(first3[1])) or \
           (is_even(first3[0]) and is_even(first3[2])) or \
           (is_even(first3[1]) and is_even(first3[2]))


def is_even(integer):
    return integer % 2 == 0


if __name__ == '__main__':
    print(find_outlier([2, 4, 6, 8, 10, 3]))
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
    print(find_outlier([0, 1, 2]))
