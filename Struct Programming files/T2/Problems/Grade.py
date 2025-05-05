grade = input("Enter a grade: ")

match (grade):
    case 'A+':
        print("For this grade, you will receive a grade points of 4.0")
    case 'A':
        print("For this grade, you will receive a grade points of 4.0")
    case 'A-':
        print("For this grade, you will receive a grade points of 3.7")
    case 'B+':
        print("For this grade, you will receive a grade points of 3.3")
    case 'B':
        print("For this grade, you will receive a grade points of 3.0")
    case 'B-':
        print("For this grade, you will receive a grade points of 2.7")
    case 'C+':
        print("For this grade, you will receive a grade points of 2.3")
    case 'C':
        print("For this grade, you will receive a grade points of 2.0")
    case 'C-':
        print("For this grade, you will receive a grade points of 1.7")
    case 'D+':
        print("For this grade, you will receive a grade points of 1.3")
    case 'D':
        print("For this grade, you will receive a grade points of 1.0")
    case 'F':
        print("For this grade, you will receive a grade points of 0")
    case _:
        print("Invalid grade entered")