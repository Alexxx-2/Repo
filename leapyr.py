current_year=int(input("which year do you want to check:"))

if(current_year %4 == 0)and (current_year %4 != 100) or (current_year%400 == 0):
    print("The year is a leap year")
else:
   print("Not a leap year")
