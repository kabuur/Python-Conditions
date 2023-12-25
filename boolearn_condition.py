
weight = 66
height = 1.85

is_raining = True

unsubscribed = False

location = "Somalia"

is_sunny = True

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "Somalia" or location == "Kenya"):
    print("send email")