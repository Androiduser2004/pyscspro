print("welcome to python database entry")

fname=(input("Enter your first name :"))
sname=(input("enter your second name:"))
class1=(input("enter your class(in roman):"))
section=(input("enter your section:"))

print('please enter your marks below')
english=(int(input('enter your english marks:')))
maths=(int(input('enter your maths marks:')))
che=(int(input('entery your chemistry marks:')))
phy=(int(input('enter your physics marks:')))

total= english+maths+che+phy

output=input('Do you want ypur total marks to be displayed with statement:')
if output == 'yes' or 'Yes' or 'y' or 'Y':
  print(fname,"of",class1,section,'has scored',total,'out of 200 in the examiniation')
else:
  print('thanks for entering your marks')