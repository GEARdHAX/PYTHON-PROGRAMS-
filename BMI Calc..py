feet = int(input(" ENTER FEET : "))
inch = int(input(" ENTER INCH : "))
feet1 = feet*0.3048
inch1 = inch*0.0254
Totalm = feet1 + inch1
print("HEIGHT TAKEN (m)",Totalm)


kg = float(input("  ENTER MASS (kg) :  "))
height = Totalm**2
bmi = kg/height
if bmi<16:
    print(bmi," : Severe Thinness -_-")
elif bmi>25:
    print(bmi, " : Overweight ;(")
else:
    print(bmi," : HEALTHY ;)")