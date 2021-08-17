sci = int(input(" ENTER SCIENCE MARKS : "))
print ("   ")
maths = int(input(" ENTER MATHS MARKS : "))
print ("   ")
sst = int(input(" ENTER SST MARKS : "))
print ("   ")
Eng = int(input(" ENTER ENG MARKS : "))
print ("   ")
hindi = int(input(" ENTER HINDI MARKS : "))
print ("   ")
result = (sci+maths+sst+Eng+hindi)/500*100
if result>37:
    print("pass: ", result,"%")
else:
    print("FAIL: ",result)