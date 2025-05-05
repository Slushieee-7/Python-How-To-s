mag = float(input("Enter an earthquake magnitude: "))

if (mag < 2.0):
    print("The earthquake is classifies as a Micro Earthquake.")
elif (mag == 2.0 or mag < 3.0):
    print("The earthquake is classified as a Very Minor Earthquake.")
elif (mag == 3.0 or mag < 4.0):
    print("The earthquake is classified as a Minor Earthquake.")
elif (mag == 4.0 or mag < 5.0):
    print("The earthquake is classified as a Light Earthquake.")
elif (mag == 5.0 or mag < 6.0):
    print("The earthquake is classified as a Moderate Earthquake.")
elif (mag == 6.0 or mag < 7.0):
    print("The earthquake is classified as a Strong Earthquake.")
elif (mag == 7.0 or mag < 8.0):
    print("The earthquake is classified as a Major Earthquake.")
elif (mag == 8.0 or mag < 10.0):
    print("The earthquake is classified as a Great Earthquake.")
else:
    print("The earthquake is classified as a Meteoric Earthquake.")