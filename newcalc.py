
pre_info= "welcome to jamilas calculator\nyoull be able to perform some simple mathematical operations using this calculator"
print(pre_info)
info_prompt= input("after reading the information above\nwould you still like to use this calculator\nyes/no ")
Yes= "yes"
No= "no"
if info_prompt== Yes:
    print(input("lets begin!!!\ninput username: "))
else:
    print("thank you\nbye!!!")
    exit()

main_1= int(input("enter a number: "))
main_2=int(input("enter your second number: "))
main3= "input an operation from the options below:\naddition(1)\nsubtraction(2)\nmultiplication(3)\ndivision(4)"
print(main3)
main4= int(input("select your option: "))
addition= 1
subtraction= 2
multiplication= 3
division= 4

if main4==addition:
    print(main_1+main_2)
if main4==subtraction:
    print(main_1-main_2)
if main4==multiplication:
    print(main_1*main_2)
if main4==division:
    print( main_1/main_2)
end= "Thank you for using jamilas calculator!!!\nPS Run the code again to use the calculator!!!"
print(end)






