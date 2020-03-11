print("\n")
twenty = input("Enter the number of twenty dollar bills. ")
ten = input("   Enter the number of ten dollar bills. ")
five = input(" Enter the number of fives dollar bills. ")
one = input("   Enter the number of one dollar bills. ")
quarter = input("           Enter the number of quarters. ")
dime = input("              Enter the number of dimes. ")
nickle = input("            Enter the number of nickles. ")
penny = input("            Enter the number of pennies. ")
total = (int(twenty)*2000)+(int(ten)*1000)+(int(five)*500)+(int(one)*100)+(int(quarter)*25)+(int(dime)*10)+(int(nickle)*5)+(int(penny)*1)
totalsmall = total//100
total = total % 100
t = total//10
total = total % 10
o = total//1
print('             Your total amount of money: $',totalsmall,".",t,o, sep='')

print("\n")
print("=============================================")
print("\n")

totaldollar = input("      Enter the total amount of dollars: ")
totalcent = input("        Enter the total amount of cents: ")

totaldollar2 = int(totaldollar)*100
totalcent2 = int(totalcent)
totaltwenty = totaldollar2//2000
totaldollar2 = totaldollar2 % 2000
totalten = totaldollar2//1000
totaldollar2 = totaldollar2 % 1000
totalfive = totaldollar2//500
totaldollar2 = totaldollar2 % 500
totalone = totaldollar2//100
totaldollar2 = totaldollar2 % 100
totalquarter = totalcent2//25
totalcent2 = totalcent2 % 25
totaldime = totalcent2//10
totalcent2 = totalcent2 % 10
totalnickle = totalcent2//5
totalcent2 = totalcent2 % 5
totalpenny = totalcent2//1
totalcent2 = totalcent2 % 1

print("                     Number of Twenties:",int(totaltwenty))
print("                         Number of Tens:",int(totalten))
print("                        Number of Fives:",int(totalfive))
print("                         Number of Ones:",int(totalone))
print("                     Number of Quarters:",int(totalquarter))
print("                        Number of Dimes:",int(totaldime))
print("                      Number of Nickles:",int(totalnickle))
print("                      Number of Pennies:",int(totalpenny))
print("\n")
