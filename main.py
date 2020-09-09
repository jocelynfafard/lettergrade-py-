def getLetterGrade(grade):
    if grade >= 93:
      return "A"
    elif 90 <= grade < 93:
      return "A-"
    elif 87 <= grade < 90:
      return "B+"
    elif 83 <= grade < 87:
      return "B"
    elif 80 <= grade < 83:
      return "B-"
    elif 77 <= grade < 80:
      return "C+"
    elif 70 <= grade < 77:
      return "C"
    elif 60 <= grade < 70:
      return "D"
    elif 60 < grade:
      return "F"
    else:
      return "F"

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")
   
if __name__ == "__main__":
 run()