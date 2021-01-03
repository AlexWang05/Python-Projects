print("This program compares two applicants to\n"
      + "determine which one seems like the stronger\n"
      + "applicant. For each candidate I will need\n"
      + "either SAT or ACT scores plus a weighted GPA.\n")  # printing required info

scoreChoice = int(input("\nInformation for the first applicant:"
                        "\n\tdo you have 1) SAT scores or 2) ACT scores? "))

# initializes element
satScore = float(0)
actScore = float(0)

if scoreChoice == 1:
    satMath = int(input("SAT Math? "))
    satVerbal = int(input("SAT Verbal? "))

    satScore = float((2 * satVerbal + satMath) / 24)  # calculate sat score

elif scoreChoice == 2:
    actEnglish = int(input("ACT English? "))
    actMath = int(input("ACT Math? "))
    actReading = int(input("ACT Reading? "))
    actScience = int(input("ACT Science? "))

    actScore = float((2 * actReading + actEnglish + actMath + actScience) / 1.8)

actualGpa = float(input("Overall GPA? "))
maxGpa = float(input("Max GPA? "))

gpaScore = float((actualGpa / maxGpa) * 100)  # calculating gpa score

overallScore1 = float(0)  # initializing overall score for student 1

if scoreChoice == 1:
    overallScore1 = satScore + gpaScore

elif scoreChoice == 2:
    overallScore1 = actScore + gpaScore

print("\nInformation for the second applicant:")
scoreChoice = int(input("\tdo you have 1) SAT scores or 2) ACT scores? "))

satScore = 0
actScore = 0

if scoreChoice == 1:
    satMath = int((input("SAT Math? ")))
    satVerbal = int((input("SAT Verbal? ")))

    satScore = float((2 * satVerbal + satMath) / 24)  # calculate sat score

elif scoreChoice == 2:
    actEnglish = int(input("ACT English? "))
    actMath = int(input("ACT Math? "))
    actReading = int(input("ACT Reading? "))
    actScience = int(input("ACT Science? "))

    actScore = float((2 * actReading + actEnglish + actMath + actScience) / 1.8)

actualGpa = float(input("Overall GPA? "))
maxGpa = float(input("Max GPA? "))

gpaScore = float((actualGpa / maxGpa) * 100)  # calculating gpa score

overallScore2 = float(0)  # initializing overall score for student 1

if scoreChoice == 1:
    overallScore2 = satScore + gpaScore

elif scoreChoice == 2:
    overallScore2 = actScore + gpaScore

print("The score for applicant 1 is " + str(overallScore1))
print("The score for applicant 2 is " + str(overallScore2))

if overallScore1 > overallScore2:
    print("The first applicant seems to be better")

elif overallScore1 < overallScore2:
    print("The second applicant seems to be better")

else:
    print("The two applicants seem to be equal")
