import math
l= []
b = int(input('ENTER "n" Resistor : '))
for num in range(b):
 print(num+1,'resistor = ',end='')
 resistor = int(input())
 l.append(resistor)
print("These are the resistors : ",l,'Ω')

decision = int(input('''      \b   EᑎTEᖇ ᑕᕼOIᑕE \nEnter '1' = Series Combination 𝙊𝙍\nEnter '2' = Parallel Comnination : '''))

def series():
  resistor = 0
  for num in l:
    resistor=resistor+num
  print('Total Resistance : ',resistor,'Ω')
#series()

def parallel():
  resistor=0
  for num in l:
    resistor = resistor+1/num
  resistor = 1/resistor
  print(round(resistor,2),'Ω')
#parallel()

if decision==1:
  series()
else:
  parallel()

