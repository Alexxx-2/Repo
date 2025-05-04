for i in range(5):
    current_year = int(input("Which year do you want to check: "))

    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        print("The year is a leap year")
    else:
        print("Not a leap year")
