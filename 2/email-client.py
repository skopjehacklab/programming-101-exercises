# Imagine you're writing an email client. All of the messages are kept
# in a list of dictionaries, and each dict contains info about the
# message.
#
# Your task is to write the code responsible for printing the
# messages in a user-friendly way.
#
# The program should print:
#
#   You have 3 unread messages.
#
#   Messages:
#   * Hey bro! (asdf.person@gmail.com)
#   * [unread] Free nigerian monies! (random19@yahoo.com)
#   * [unread] Newsletter: why code never works (bleh-blah@gmail.com)
#   * This is a test! (testingemail123@gmail.com)
#
# The number of unread messages should be calculated based on the `was_opened`
# field in the dict.
#
# Bonus:
# a) Print "You have no new messages" instead of "You have 0 unread messages"
# b) Print the messages sorted by date (newest first)
# c) Try to detect spam (any message that contains "free" or "dollar"
#    in the body can be considered spam). If it's spam, add "[spam]" in front
#    of the subject.

msgs = [
    {
        'from': 'asdf.person@gmail.com',
        'subject': 'Hey bro!',
        'body': "What's up?",
        'was_opened': False,
        'date': { 'd': 30, 'm': 6, 'y': 2015 }
    },
    {
        'from': 'random19@yahoo.com',
        'subject': 'Free nigerian monies!',
        'body': "My uncle died and wants to transfer some dollars..",
        'was_opened': True,
        'date': { 'd': 5, 'm': 6, 'y': 2014 }
    },
    {
        'from': 'bleh-blah@gmail.com',
        'subject': 'Newsletter: why code never works',
        'body': "Because PHP...",
        'was_opened': True,
        'date': { 'd': 19, 'm': 11, 'y': 2015 }
    },
    {
        'from': 'testingemail123@gmail.com',
        'subject': 'This is a test',
        'body': "ASDASDASD",
        'was_opened': False,
        'date': { 'd': 3, 'm': 2, 'y': 2015 }
    }
]


# Write your code here