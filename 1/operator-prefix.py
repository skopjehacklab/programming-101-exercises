def find_operator(number):
    pass

# Tests
assert(find_operator('070-222-111') == 'Operator A')
assert(find_operator('071-111-222') == 'Operator A')
assert(find_operator('072-111-222') == 'Operator A')
assert(find_operator('075-234-567') == 'Operator B')
assert(find_operator('076-321-321') == 'Operator B')
assert(find_operator('077-999-999') == 'Operator C')
assert(find_operator('078-123-000') == 'Operator C')
print('Works!')
