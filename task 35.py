day = str(input(" enter the day :"))
if day in ['Monday', 'Tuesday',  'Wednesday',  'Thursday']:
    print('weekday')
elif day == "Friday":
    print('TGIF')
elif day in ['Saturday', 'sunday']:
    print("weekend")
else:
    print("invalid score")
