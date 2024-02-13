import datetime

x = datetime.datetime.now()

print(x.strftime("%a"))#Weekday, short version
#Wed
print(x.strftime("%A"))#Weekday, full version
#Wednesday
print(x.strftime("%w"))#Weekday as a number 0-6, 0 is Sunday
#3
print(x.strftime("%d"))#Day of month 01-31
#14  
print(x.strftime("%b"))#Month name, short version 
#Feb   