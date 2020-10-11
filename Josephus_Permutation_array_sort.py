# Josephus Permutation
# return every k element from exist array
def josephus(items, k):
    number, new_list = 0, []

    if not items:
        return []
    else:
        while len(items) > 0:
            number = (number + k - 1) % len(items)
            new_list.append(items.pop(number))
        # print(new_list)
    return new_list


josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
