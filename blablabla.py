#Names:Tommy
#Date:3/20/2024
#Purpose: Review Question 1
year = int(input("What is the year? (Enter the last two digits of the year) "))
month = int(input("What is the month? "))
day = int(input("What is the day? "))
if month * day == year:
    print("The date is magic.")
else:
    print("The date is not a magic")