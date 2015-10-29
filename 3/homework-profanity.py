# Profanity filter
#
#
# Imagine you're writing a chat client. Each time it receives
# a message, it's represented as a list of strings.
#
# Your task is to implement a profanity filter, which -
# when enabled - will replace all the "bad" words with ****.
#
# When `profanity_filter_on` is set to `True`, the profanity
# filter is enabled. When it's `False`, bad words should
# not be replaced.
#
# Hints:
# * Use `apppend` to add a new element to a list.
#   Here's how it works:
#     >>> l = []
#     >>> l.append("first")
#     >>> print(l)
#     ["first"]
#     >>> l.append("second")
#     >>> print(l)
#     ["first", "second"]
#
#   Lists have other "special" functions too, like `count`, but
#   we'll talk about that later.
#
# * There will be two loops: one that goes through the words
#   of the sentence, and another through the list of "bad" words
# * The result should be a new list
#
# Bonus:
# * Instead of printing ['this', course, '****', 'sucks'],
#   print a proper string: "this course **** sucks"
# * If the word has `n` letters, print `n` stars:
#     "fucking" -> "*******"

bad_words = ['list', 'of', 'bad', 'words']
profanity_filter_on = True

sentence = ['this', 'is', 'a', 'bad', 'sentence']
filtered_sentence = []


# your code goes here


# It should print: ["this", "is", "a", "****", "sentence"]
# because "bad" is in the list of bad words
print(filtered_sentence)