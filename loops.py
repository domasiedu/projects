#For loops variations
''''
for i in [2, 4, 6, 8, 10]:
    print("i = ", i)

for j in range(5, 10):
    print("j = ", j)

for m in range(6, 12):
    print("Is m Even ? ", ((m % 2 == 0)))

for k in range(1, 21):
    if(k % 2) != 0:
        print("k =", k)

#Acepting float and rounding upto 2 Decimal Places
your_float = input("Enter a float :")
your_float = float(your_float)
print("Rounded to 2 Decimals : {:.2f}".format(your_float))
'''

#Investment calculation after 10 years

money_invested = input("How much to invest : ")
interest_rate = interest_rate * .01

for h in range(10):
    money_invested = money_invested + (money_invested * interest_rate)

print("Investment after 10 years will be : {:.2f}".format(money_invested), )
