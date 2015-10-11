import sys
import random

number_of_students = int(sys.argv[1])
student_ids = list(range(number_of_students))
random.shuffle(student_ids)

for sid in student_ids:
    print(sid)
    input("paused.")

print("done.")
