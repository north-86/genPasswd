import sys
import random

print(' * ' * 10, 'Password generator', ' * ' * 10)

while True:
    try:
        countPwd = int(input('Enter the number of characters for the generated password: '))
    except ValueError:
        print('Enter a number')
    else:
        break
    
if (0 < countPwd <= 20):
    print('Easy password -->\n')
elif (20 < countPwd <= 50):
    print('Medium password -->\n')
elif (50 < countPwd < 217):
    print('Complex password -->\n')
elif (countPwd == 0):
    print('Empty')
elif (countPwd >= 217):
    print('Invalid number')
    sys.exit()
elif (countPwd < 0):
    print('Invalid number. Negative number')
    sys.exit()

seq1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

seq2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

seq3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

seq4 = ['_', '&', '#', '@', '$', '?']

seqTotal = (seq1 * 3) + (seq2 * 3) + (seq3 * 3) + (seq4 * 5)

seqPassword = random.sample(seqTotal, countPwd)

password = ""

for i in seqPassword:
    print(i, sep='', end='')
    password += i

with open("Password.txt", "a") as password_file:
    print(password, file = password_file)
        
print('\n\nDone')
input()