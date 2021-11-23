from pyfiglet import figlet_format,Figlet
from termcolor import colored

print((colored(figlet_format("WELCOME",font='cyberlarge'), color="green")))

# MEASUREMENT OF HEIGHT AND CONVERSION TO (m) :-

feet = int(input(" ENTER FEET : "))
inch = int(input(" ENTER INCH : "))
feet1 = feet*0.3048
inch1 = inch*0.0254
Totalm = feet1 + inch1
print((colored(figlet_format("METERS",font='cybermedium'), color="red")),Totalm)

# MEASUREMENT OF KG AND FINAL RESULTS :-
print("")
print("")
kg = float(input("  ENTER MASS (kg) :  "))
height = Totalm**2
bmi = kg/height
if bmi<16:
    print(bmi)
    print("")
    print((colored(figlet_format("Severe thinness",font='cybermedium'), color="red")))
elif bmi>25:
    print(bmi)
    print("")
    print((colored(figlet_format("Overweight",font='cybermedium'), color="red")))
else:
    print(bmi)
    print("")
    print((colored(figlet_format("HEALTHY",font='cybermedium'), color="red")))