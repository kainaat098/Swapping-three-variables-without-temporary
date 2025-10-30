number_1=int(input("Enter the first number : "))
number_2=int(input("Enter the second number : "))
number_3=int(input("Enter the third number : "))

number_1= number_1+number_2+number_3
number_2= number_1 - (number_2+number_3)
number_3= number_1 - (number_2+number_3)
number_1= number_1 - (number_2+number_3)

print(f"{number_1}\n{number_2}\n{number_3}")