
while True:
  print('First, enter your name:')
  x = input()
  try:
    if(not x.isalpha()):
      print("Error: Contains numbers! Please use only letters.")
      x = input("Enter your name again:")
    else:
      print('Hello, ' +x+'! Welcome to Python Counting Program')
  except ValueError:
    continue

print('Now, enter any number:')
y = input()
i = 0
if(not y.isnumeric()):
  print("Error: Contains letters! Please use only numbers.")
  x = input()
else:
  print('You entered ' + y + '. Here is your score:')
  while i <= int(y):
    print(i)
    i += 1


# checking for alphabets/number
#print(x.isalpha())
#print(y.isnumeric())



print('by Yuliia Poperechna')
