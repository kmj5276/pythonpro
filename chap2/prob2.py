print("                     Trust Fund Budddy")
print("\nTotals your monthly spending so that your trust fund doesn't run out")
print("<and you're forced to get a real job>.")
print("\nPlease enter the requested, monthly costs. Since you're rich, ignore pennies")
print("and use only dollar amounts.")
car = int(input("\n\nLamborghini Tune-Ups: "))
apt = int(input("Manhattan Apartment: "))
rnt = int(input("Private Jet Rental: "))
gif = int(input("Gifts: "))
din = int(input("Dinnig Out: "))
sta = int(input("Staff <butlers, chef, driver, assistant>: "))
per = int(input("Personal Guru and Coach: "))
com = int(input("Computer Games: "))
total = car + apt + rnt + gif + din + sta + per + com
print("\nGrand Total: ", total)
