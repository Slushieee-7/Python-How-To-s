month = int(input("Please enter your month of birth as a number: "))
day = int(input("Please enter your day of birth as a number: "))

match (month):
    case 1:
        if (day <= 19):
            print("You are a Capricorn")
        elif (day <= 31):
            print("You are an Aquarius")
        else:
            print("Invalid day of birth")
    case 2:
        if (day <= 18):
            print("You are an Aquarius")
        elif (day <= 28):
            print("You are a Pisces")
        else:
            print("Invalid day of birth")
    case 3:
        if (day <= 20):
            print("You are a Pisces")
        elif (day <= 31):
            print("You are an Aries")
        else:
            print("Invalid day of birth")
    case 4:
        if (day <= 19):
            print("You are an Aries")
        elif (day <= 30):
            print("You are a Taurus")
        else:
            print("Invalid day of birth")
    case 5:
        if (day <= 20):
            print("You are an Taurus")
        elif (day <= 31):
            print("You are a Gemini")
        else:
            print("Invalid day of birth")
    case 6: #June
        if (day <= 20):
            print("You are a Gemini")
        elif (day <= 30):
            print("You are a Cancer")
        else:
            print("Invalid day of birth")
    case 7: #July
        if (day <= 22):
            print("You are an Cancer")
        elif (day <= 31):
            print("You are a Leo")
        else:
            print("Invalid day of birth")
    case 8: #August
        if (day <= 22):
            print("You are a Leo")
        elif (day <= 31):
            print("You are a Virgo")
        else:
            print("Invalid day of birth")
    case 9: #September
        if (day <= 22):
            print("You are a Virgo")
        elif (day <= 30):
            print("You are a Libra")
        else:
            print("Invalid day of birth")
    case 10: #October
        if (day <= 22):
            print("You are a Libra")
        elif (day <= 31):
            print("You are a Scorpio")
        else:
            print("Invalid day of birth")
    case 11: #November
        if (day <= 21):
            print("You are a Scorpio")
        elif (day <= 30):
            print("You are a Sagittarius")
        else:
            print("Invalid day of birth")
    case 12: #December
        if (day <= 21):
            print("You are a Sagittarius")
        elif (day <= 31):
            print("You are a Capricorn")
        else:
            print("Invalid day of birth")
    case _:
        print("Invalid month of birth")
