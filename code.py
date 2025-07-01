import random
chars='abcdefghijklmnopqurstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789!@#$%^&*()[]{}'
Length=int(input('Enter The Length Password: '))
Password=''
for i in range(Length):
 Password+=random.choice(chars)
print( 'Your Password:',Password)