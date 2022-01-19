#Katie Frymire
#1/19/22

# Other operators +-*/ exponents % modulus, Format printing, escape character

#Program creating an equation, asking user input, and formatting the output

import os
os.system ('cls')

#Declare varibles

var1=10
var2=2
var3=2.9
var4=5

#Calculate equation


Result= (3*var1 - 2*(var2)**2 /var3)/var4

#Printing Formats

print("var1=", var1) 
print("var2=", var2)
print("var3= %.0f"% var3) 
print("var4=", var4)
print("The result of ((3*var1 - 2*(var2)**2 /var3)/var4) is  %6.3F"% Result, end="------")

print("\n The \"quotes\" tabs \t backlash \\")

