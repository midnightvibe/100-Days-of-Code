student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
flag = 0
for height in student_heights:
   sum_height = sum_height + height
   flag = flag + 1

average_height = sum_height/flag
print(round(average_height))
