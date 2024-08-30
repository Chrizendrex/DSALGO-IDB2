#This is how to comment
'''This is a multiline comment'''
'''
value= 1;
value2= 2;
value3= value * value2;
    print(" ",value3,"\n test");
        userin=input("Enter your age;"); #getting an input
    print(userin); #prints out userin
        userin1= int(input("Enetr your lucky number"));
    print(userin1);
'''
#100pesos nintendo wii
'''
ninWii= 100
    print("Hello, this is nintendo store, Welcome!")
    print("-----------------------------------------------")
    print("I see that you are buying a nintendo wii!")
    print("-----------------------------------------------")
userMon=int(input("Can you please enter the amount of your money?"))
    print("Nintendo Wii is 100 PHP")
afford=ninWii-(userMon%ninWii)
userBuy= int(userMon/ninWii)
    print("You can buy ",userBuy)
    print("Your money is lacking: ",afford,"PHP.")
'''

'''
fact=1
until=int(input("until what number: "))
for x in range(1, until+1):
    fact = fact * x

print("Factorial of", until,"is:", fact)
'''

factorList= []
userIn=int(input("Enter a number:"))
for a in range (1,userIn+1):
    if userIn%a==0:
        factorList.append(a)

print("Factor of", userIn, " are:", factorList)











