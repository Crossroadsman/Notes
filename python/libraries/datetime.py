from datetime import date     # from the datetime module import the date class
from datetime import time
from datetime import datetime 

today = date.today()
print("Today's date is", today) # date.today() prints as yyyy-mm-dd

print("Date components: )
print(today.year, today.month, today.day) # components are ints corresponding to the actual component value, e.g., july is 7, 2017 is 2017, 3rd day of the month is 3, etc.

today.weekday() // zero-based index of the day in the working week (i.e., Monday is 0, Sunday is 6)
