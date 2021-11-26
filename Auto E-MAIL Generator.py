from pyfiglet import figlet_format,Figlet
from termcolor import colored
import re

# MAIN CODE......... 

print((colored(figlet_format("SIR. ADARSH"), color="green")))

letter = '''(Your Name)
(Address)
(Phone Number)
(E-mail)

(date)

(Name of Receiver)
(Title)
(Company Name)
(Address)

Dear (Name of Receiver),

When writing a letter using block form, no lines are indented. Include your name, address, and phone number where you can be contacted, as well as the date. You then include the name and address of the person you are sending the letter to.

With new paragraphs, just skip a line instead of indenting.

Add your phone number where you can be contacted in the last paragraph. If the receiver needs to use a relay service to call you, briefly explain that you are deaf/ hard-of-hearing and that s/he can call you through relay. Give the receiver his/her state relay number and explain that s/he will need to give the operator your number. Then give him/her your number.

Sincerely,

(Your Name)
(Your Title)
'''
name = input(" ENTER YOUR NAME : ")
place = input(" ENTER PLACE NAME : ")
date = input(" ENTER DATE : ")
# ↓ PHONE NUMBER CODE :-
ph= (input(" ENTER NO. : "))
regex = re.compile('[0,1,2,3,4,5,6,7,8,9]')
if (regex.search(ph) == None):
    print(" PHONE NUMBER CAN'T CONTAIN CHARACTERS ;(")
elif len(ph)==10:
    print('')
else:
    print(" ENTER PROPER PHONE NO. OF 10 ;) ")
    exit()
# ↓ EMAIL CODE :-
email = input("ENTER E-MAIL : ")
regex = re.compile('[@]')
if (regex.search(email) == None):
    print(" NOT CONTAINS '@'. Enter Proper E-MAIL :)")
    exit()
receiver = input(" ENTER Name of Receiver : ")
Title = input(" ENTER TITLE : ")
Company = input(" ENTER Company Name : ")
ytitle = input(" ENTER Your Title : ")
print('')

# ↓ REPLACEMENT & ↑ INPUTS............

letter = letter.replace("(Your Name)", name)
letter = letter.replace("(Address)", place)
letter = letter.replace("(date)", date)
letter =  letter.replace("(Phone Number)", ph)
letter = letter.replace('(E-mail)', email)
letter = letter.replace('(Name of Receiver)', receiver)
letter = letter.replace('(Title)', Title)
letter = letter.replace('(Company Name)', Company)
letter = letter.replace('(Your Title)', ytitle)
print('')
print((colored(figlet_format("LETTER",font='banner3'), color="green")))
print('')
print(letter)