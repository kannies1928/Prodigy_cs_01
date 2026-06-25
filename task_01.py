temp=float(input("enter the temperature value : "))
unit =input("enter the unit (C/F/K):").upper()

if unit =="C":
    fahrenheit =(temp*9/5)+32
    kelvin=temp+273.15
    print("fahrenheit:",fahrenheit,)
    print("kelvin:",kelvin)

elif unit =="F":
    celsius=(temp-32)*5/9
    kelvin=celsius+273.15
    print("celsius:",celsius)  
    print("kelvin:",kelvin)  
    

elif unit =="K":
    celsius=temp-273.15
    fahrenheit=(celsius*9/5)+32
    print("celsius:",celsius)  
    print("fahrenheit:",fahrenheit,)

else:
  print("invalid unit! please enter c, f, or k:")