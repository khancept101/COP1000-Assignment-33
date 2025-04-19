# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# Get the year, then the month, then the day
year  = int(input("Enter year: "))
month = int(input("Enter month: "))
day   = int(input("Enter day: "))

# Check to be sure date is valid

if year <= MIN_YEAR: # invalid year
    validDate = False
elif month < MIN_MONTH or month > MAX_MONTH: # invalid month
    validDate = False
else:
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            MAX_DAY = 29
        else:
            MAX_DAY = 28
    elif month in (4, 6, 9, 11):
        MAX_DAY = 30
    else:
        MAX_DAY = 31
    if day < MIN_DAY or day > MAX_DAY: # invalid day
        validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date.")