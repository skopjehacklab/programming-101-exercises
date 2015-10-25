# Building X has an electronic door mechanism. Only people
# on the whitelist can enter the building.
#
# Your task is to write a function that checks if the
# person trying to enter the building is on the whitelist.
#
# Complete the function: given a username and their password,
# it checks if the user has supplied the correct password.
#
# Returns `True` or `False`, depending on whether they're
# allowed to enter or not.


def enter(username, password):
    whitelist = [
        { 'user': 'killy', 'age': 29, 'password': 'youshallnotpass' },
        { 'user': 'hacker', 'age': 17, 'password': 't00str0ng1' },
        { 'user': 'whoeverest', 'age': 25, 'password': 'blahbleh' }
    ]

    pass # delete "pass" and write your code here


# Tests (do NOT edit!)

res1 = enter('killy', 'youshallnotpass')
res2 = enter('whoeverest', 'youshallnotpass')
res3 = enter('hacker', '12312321')

assert(res1 == True)
assert(res2 == False)
assert(res3 == False)
print("Access granted.")
