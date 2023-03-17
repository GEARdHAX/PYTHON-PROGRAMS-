import stack
# <=========Pushing Values===========>
def push(x):
    n = int(input('ENTER NUMBER :'))
    x.append(n)
    
# <===========Poping Values============>
def pop(x):
    if x==[]:
        print("Can't delete, empty stack!")
    else:
        x.pop()

# <=============Peek Value============>
def peek(x):
    # print('Last element of stack : ',x.pop()) ===> Alternate method!
    return x[-1]

# <==============Traverse Values===============>
def traverse(x):
    a = len(x)
    print('All the values of list : ')
    for i in range(0,a):
        print(x[i],end=' , ')

# <==========Global Stack=============>

my_list = []

# take user input for the number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# use a for loop to iterate n times and take user input for each element
for i in range(n):
    element = input("Enter an element for the list: ")
    my_list.append(element)

# print the final list
print("The final list is:", my_list)
print(' ')


# my_list = [1,2,3,4,5]
push(my_list)
print(' ')
print('Pushed Value : ',my_list)
pop(my_list)
print(' ')
print('Poped Value : ',my_list)
print(' ')
print('Last or Top most value : ',peek(my_list))
print(' ')
traverse(my_list)