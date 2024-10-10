def min_(x):
    return min(x)


def max_(x):
    return max(x)


def len_(x):
    return len(x)


def sum_(x):
    return sum(x)


def sorted_(x):
    return sorted(x)


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        result = func(int_list)
        results.update({func.__name__[:-1]: result})

    return results


print(apply_all_func([6, 20, 15, 9], max_, min_))
print(apply_all_func([6, 20, 15, 9], len_, sum_, sorted_))
