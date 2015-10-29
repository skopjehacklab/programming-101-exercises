# Blocked users
#
#
# One of the core features of every chat client is the ability to
# block certain users. Once you've blocked somebody, their messages
# should no longer appear in the chat.
#
# A conversation is a list of messages; every message is a dict:
#   { 'username': 'whoeverest', 'msg': 'Hey there' }
#
# Blocked users are kept in a list:
#   blocked_users = ['user1', 'user2', 'user3']
#
# Write a program that will print the conversation
# in this format: "username: msg"
#
# If the user is blocked, their message won't get printed.


blocked_users = ['whoeverest', 'someone']
conversation = [
  { 'user': 'whoeverest', 'msg': 'hey dude! where did you disappear?' },
  { 'user': 'tom', 'msg': 'you awake?' },
  { 'user': 'tom', 'msg': 'i am up already' }
]


# Your code goes here.


# When executed, this program should print:
#
# $ python3 homework-blocked.py
# tom: you awake?
# tom: i am up already
#
# Note: whoeverest is ignored, because he's in the `blocked_users`
# list.