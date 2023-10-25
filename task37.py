month = input("enter the month :")
if month in ["january", "february", "march", "april", "may"]:
    print ("spring")
elif month in ["june", "july", "august"]:
    print("summer")
elif month in ["september", "october", "november"]:
    print("fall")
elif month == "december":
    print("winter")
else:
    print("invaild month")