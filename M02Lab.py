# Author: Jenna Helm
# File Name: M02Lab.py
# Description: This application will use a student's name inputted and GPA using a decimal float in order to identify if they make Dean's List or Honor Roll.

# Repository: https://github.com/Jenna-Helm/GitSDEV220

#Create a loop that is only cancelled when ZZZ is typed
while True:
   last_name = input("Enter the student's Last Name. To quit, enter 'ZZZ': ")
   if last_name == 'ZZZ':
       print("Student information has been quit.")
       break
   first_name = input("Enter the student's first name: ")
   try:
    # GPA should be a float number as it contains a decimal
       gpa = float(input("Enter the student's GPA: "))
    # Added value information to catch any value entry errors that would not count as a numeric value
   except ValueError:
       print("GPA contains a entry that is not a numberic value")
       continue
   if gpa >= 3.5:
       print(f"Congratulations! {first_name} {last_name} has made the Dean's List!")
   elif gpa >= 3.25:
       print(f"Congratulations! {first_name} {last_name} has made the Honor Roll!")
   else:
       print(f"Unfortunately, {first_name} {last_name} hasn't qualified for Dean's List or Honor Roll.")