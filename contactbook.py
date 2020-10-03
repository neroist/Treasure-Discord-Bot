



def book():
  contactName = input('''Name:
  ''')

  contactNumber = input('''
  Phone Number:
  ''')

  contactEmail = input('''
  Email:
  ''')

  oen = open('ContactBook.txt')
  oen.write(f'''
  Name: {contactName}
  Phone Number: {contactNumber}
  Email: {contactEmail}

  ''')
  oen.close()
  q = input('See contact book?')
  if q == 'yes' :
    print(oen.read())


def write():
    x = input()
    y = open('notepadcopy.txt', 'x')
    y.write(f'''x

    ''')

inout = input('''write or contact book:

''')
if inout == 'write':
    write()
elif inout == 'contact book':
    book()


