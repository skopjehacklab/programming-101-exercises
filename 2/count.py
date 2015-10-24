# Complete the function: when given a list (`lst`) and
# some element (`el`), the function should count how many
# times `el` is found in the list.
#
# For example, in the list ["MDMA", "MDA", "LSD", "DMT", "MDA"]
# the string "MDA" is found two times, and "LSD" is found once.
#
# So if we write:
#
# >>> n = count(["MDMA", "MDA", "LSD", "DMT", "MDA"], "MDA")
# >>> print(n)
#
# it should print: 2
#
# Hint: you should combine a condition (if) and a loop (for).


def count(lst, el):
    pass # delete "pass" and write your code here


# Tests (do NOT edit!)

r1 = count([1,2,3], 2)
r2 = count([1, 1, 1, 1, 1], 1)
r3 = count(["A", "B", "C", "A", "C"], "D")

assert(r1 == 1)
assert(r2 == 5)
assert(r3 == 0)

print("Yep, that's it.")