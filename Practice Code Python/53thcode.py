def is_leap(year):
    # leap = False
     
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return 'Its not a leap year'
        else: 
            return 'Its a leap year'
    else:
        return 'Its not a leap year'
     
        return leap

year = int(input("enter a Year to check if it's a leap year or not: "))
print(is_leap(year))


