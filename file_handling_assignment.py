
# #File creation and writing onto it
try:
    with open('my_file.txt','w') as f:
        f.write('My name is Daniel Chacha. \n I am 20 years old. \n I love Kenya.')
except IOError:
    print('Error could not create the file')
finally:
    print('Exited Successfully')
   
# #File reading and display
try:
    with open('my_file.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('Error: No such file')
finally:
    print('Exited Successfully')

#File Appending
try:
    with open('my_file.txt' ,'a') as f:
        f.write('\nI am a student at Multimedia University of Kenya. \n A second year. \n Pursing a Bachelors Degree in Computer Science')
except PermissionError:
    print('Error! Permission Denied')
finally:
    print('Exited Successfully')
