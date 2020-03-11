print("Please enter the quantity for each of the indicated denominations.")
Twentys =      int(input("Twenty Dollar Bills: "))
Tens =         int(input("   Ten Dollar Bills: "))
Fives =        int(input("  Five Dollar Bills: "))
Twos =         int(input("   Two Dollar Bills: "))
Ones =         int(input("   One Dollar Bills: "))
Half_Dollars = int(input("       Half-Dollars: "))
Quarters =     int(input("           Quarters: "))
Dimes =        int(input("              Dimes: "))
Nickels =      int(input("            Nickels: "))
Pennies =      int(input("            Pennies: "))
#This part is a little akward/messy, but functional. If you can clean it up and still have it work go right on ahead
#Total = (Twentys*2000)+(Tens*1000)+(Fives*500)+(Ones*100)+(Quarters*25)+(Dimes*10)+(Nickels*5)+(Pennies*1)
Total = (Twentys*2000)+(Tens*1000)+(Fives*500)+(Twos*200)+(Ones*100)+(Half_Dollars*50)+(Quarters*25)+(Dimes*10)+(Nickels*5)+(Pennies*1)
d     = Total//100
Total = Total % 100
t     = Total//10
Total = Total % 10
o     = Total//1
print("The Amount of Cash You Entered was: $",d,".",t,o, sep='')
#Line Seperates Part 1 from Part 2
print("-------------------------------------------------------------------------------")
Money = input("Please enter the cash value without the '$' (i.e. 345.23): ")
Cash   = float(Money)*100
Cents  = int(round(Cash))
pTwentys      = Cents//2000
Cents       = Cents % 2000
pTens         = Cents//1000
Cents       = Cents % 1000
pFives        = Cents//500
Cents       = Cents % 500
pTwos         = Cents//200
Cents       = Cents % 200
pOnes         = Cents//100
Cents         = Cents % 100
pHalf_Dollars = Cents//50
Cents         = Cents % 50
pQuarters     = Cents//25
Cents         = Cents % 25
pDimes        = Cents//10
Cents         = Cents % 10
pNickels      = Cents//5
Cents         = Cents % 5
pPennies      = Cents//1
print("Twenty Dollar Bills:", pTwentys)
print("   Ten Dollar Bills:", pTens)
print("  Five Dollar Bills:", pFives)
print("   Two Dollar Bills:", pTwos)
print("   One Dollar Bills:", pOnes)
print("       Half-Dollars:", pHalf_Dollars)
print("           Quarters:", pQuarters)
print("              Dimes:", pDimes)
print("            Nickels:", pNickels)
print("            Pennies:", pPennies)