# def apply_all_func(int_list, *functions):
#     print(functions)
#     results = {}
#     for i in functions:
#         print(i)
#         solution = map(i.__name__, int_list)
#         results.update({i: solution})
#
#     return results




# def min(x):
#     return min(x)
#
#
def max(x):
    return max(x)

#
# def len(x):
#     return len(x)
#
#
# def sum(x):
#     return sum(x)
#
#
# def sorted(x):
#     return list(sorted(x))


a = [6, 20, 15, 9]
result = map(max, a)
print(list(result))
# print(apply_all_func([6, 20, 15, 9], max, min))
# print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
