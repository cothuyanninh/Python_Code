import datetime
year_now = datetime.date.today().year
_name = input("What is your name: ")
_age =  int(input("How old are you?:"))

print("Hi %s. You will be 100 years old in: %d"%(_name, year_now + (100-_age)))