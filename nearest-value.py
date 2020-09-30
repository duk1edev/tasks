def nearest_value(values: set, one: int) -> int:
    # your code here

    num_lst = list(values)

    if one in num_lst:
        return one
    else:
        if one >= 0:
            if one < max(num_lst):
                for i in range(max(num_lst)):
                    if one - i in num_lst:
                        return one - i
                    elif one + i in num_lst:
                        return one + i
            else:
                for i in range(one):
                    if one - i in num_lst:
                        return one - i
                    elif one + i in num_lst:
                        return one + i

        else:
            if one < max(num_lst) and max(num_lst) != 0:
                for i in range(max(num_lst)):
                    if one + (i * (-1)) in num_lst:
                        return one + (i * (-1))
                    elif one + i in values:
                        return one + i
            elif one > max(num_lst):
                for i in range((one)):
                    if one + (i * (-1)) in num_lst:
                        return one + (i * (-1))
                    elif one + i in num_lst:
                        return one + i
            else:
                for i in range(abs(min(num_lst))):
                    if one + (i * (-1)) in num_lst:
                        return one + (i * (-1))
                    elif one + i in values:
                        return one + i


if __name__ == '__main__':
    print("Example:")
    print(nearest_value([0,3, 2, -2], 56))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
