letters =['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','=','+','_','{','}','[',']',':',';',"'",'"',',','.','<','>','/','?']

import random
import string

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))



linp=[]
for chhar in range(0,nr_letters):
    linp.append(random.choice(letters))

sinp=[]
for chhar in range(0,nr_symbols):
    sinp.append(random.choice(symbols))

ninp=[]
for chhar in range(0,nr_numbers):
    ninp.append(random.choice(numbers))

gen_pwd = ''.join(linp) + ''.join(sinp) + ''.join(ninp)

print("Your password is: " + gen_pwd + "\n" +" (Easy to remember)")
a_pwd = list(gen_pwd)
random.shuffle(a_pwd)
print("Your password is: " + ''.join(a_pwd) + "\n" +" (Hard to guess)")