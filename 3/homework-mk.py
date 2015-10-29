# -*- coding: utf-8 -*-

# MK cyrillic to latin transliteration
#
#
# You're given a large string of text, written in Macedonian.
# Your job is to write a program that converts cyrillic letters to latin.
#
# E.g. if the sentence is "Чекај малку, што правам?",
# it should print:
#   Chekaj malku, shto pravam?
#
# Here's the character map:
#
# ѓ -> gj     ж -> zh     ѕ - dz     љ -> lj     њ -> nj
# ќ -> kj     ч -> ch     џ - dzh    ш -> sh
#
# Hints:
# * `for` loops can be used on strings
# * You can use a dictionary to map between the cyrillic -> latin pairs
# * Alternatively, you can write a bunch of `if` statements
# * Be sure to handle uppercase letters!

sentence = 'Чекај малку, што правам?'
new_sentence = ''


# your code goes here


print(new_sentence) # should print 'Chekaj malku, shto pravam?'