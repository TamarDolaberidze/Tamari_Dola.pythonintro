import datetime

birth_year = int (input("please enter your birth year: "))
birth_month = int (input("please enter your birth month: "))
birth_day = int (input("please enter your birth day: "))

birth_date = datetime.datetime(birth_year, birth_month, birth_day)
week_day = birth_date.strftime("%A")
print (week_day) 

