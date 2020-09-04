# Author Joshua McIntyre


gradepoint1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
credit1 = float(credit1)
if(gradepoint1 == "A"):
  gradepoint1 = 4.0
elif(gradepoint1 == "A-"):
  gradepoint1 = 3.67
elif(gradepoint1 == "B+"):
  gradepoint1 = 3.33
elif(gradepoint1 == "B"):
  gradepoint1 = 3.0
elif(gradepoint1 == "C+"):
  gradepoint1 = 2.33
elif(gradepoint1 == "C"):
  gradepoint1 = 2.0
elif(gradepoint1 == "D"):
  gradepoint1 = 1.0
else:
   gradepoint1 = 0.0

print(f"Grade point for course 1 is: {gradepoint1}")

gradepoint = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)
if(gradepoint2 == "A"):
  gradepoint2 = 4.0
if(gradepoint2 == "A-"):
   gradepoint2 = 3.67
if(gradepoint2 == "B+"):
   gradepoint2 = 3.33
if(gradepoint2 == "B"):
   gradepoint2 = 3.0
if(gradepoint2 == "B-"):
   gradepoint2 = 2.67
if(gradepoint2 == "C+"):
  gradepoint2 = 2.33
if(gradepoint2 == "C"):
   gradepoint2 = 2.0
if(gradepoint2 == "D"):
   gradepoint2 = 1.0
else: 
  gradepoint2 = 0.0

print(f"Grade Point for course is: {gradepoint2}")

gradepoint3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ") 
credit3 = float(credit3)
if(gradepoint3 == "A"): 
  gradepoint3 = 3.33
elif(gradepoint3 == "A-"):
  gradepoint3 = 3.67
elif(gradepoint3 == "B+"):
  gradepoint3 = 3.33
elif(gradepoint3 == "B"):
  gradepoint3 = 3.00
elif(gradepoint3 == "B-"):
  gradepoint3 = 2.67
elif(gradepoint3 == "C+"):
  gradepoint3 = 2.33
elif(gradepoint3 == "C"):
  gradepoint3 = 2.0
elif(gradepoint3 == "D"):
  gradepoint3 = 1.0
else:
  gradepoint3 = 0.0

  print(f"Grade point for course 3 is: {gradepoint3}")

  gradepoint1 = float(gradepoint1)
  gradepoint2 = float(gradepoint2)
  gradepoint3 = float(gradepoint3)

  gpa = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)
  print(f"Your gpa is: {gpa}")












