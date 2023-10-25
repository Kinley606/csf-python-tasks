temperature = int (input("enter the temperature :"))
if temperature >= 100 :
    print("Boiling")
elif temperature >=32 and temperature <=99 :
    print(" Liquid")
else:
    print(" Freezing")