# The objective of this excercise is to create a data structure
# that will contain personal information about people.
#
# These are the requirements:
#
# * We want people's personal info to be kept in a dictionary (dict) called "people"
# * Each person has a unique ID number (e.g '123') and it will be used as a KEY in the dict
# * The VALUE should be another dictionary containing these keys:
#     'name', 'surname', 'age', 'weight', 'is_married' and 'children'
#
# Types:
# * The type of 'name' and 'surname' should be of type string
# * 'age' should be an integer
# * 'weight' should be a float
# * 'is_married' should be a bolean
# * 'children' should be a list of dictionaries, each of them containing
#   personal information about the child
# * The dictionary that contains the child's information should have
#   the same structure as a person (name, surname, age etc.)
# * A child should have NO children itself; that value should be an empty list
#
#
# Your task is to create this type of a structure and fill it with
# information about two people:
#
# * The first person has id '123'
# * The second person has id '456'
# * Person with id == '123' has TWO children
# * Person with id == '456' has ONE child
#
# Pick the rest of the values yourself. :-)


people = {}
# Delete this comment and WRITE YOUR CODE HERE.


# TESTS (don't edit)

assert(type(people) == dict)

p1 = people['123']
assert(type(p1['name']) == str)
assert(type(p1['surname']) == str)
assert(type(p1['age']) == int)
assert(type(p1['weight']) == float)
assert(type(p1['is_married']) == bool)
assert(type(p1['children']) == list)
assert(len(p1['children']) == 2)

c1 = p1['children'][0]
assert(type(c1) == dict)
assert(type(c1['name']) == str)
assert(type(c1['surname']) == str)
assert(type(c1['age']) == int)
assert(type(c1['weight']) == float)
assert(type(c1['is_married']) == bool)
assert(c1['children'] == [])

p2 = people['456']
assert(len(p2['children']) == 1)

print('Awesome, good job. :)')
