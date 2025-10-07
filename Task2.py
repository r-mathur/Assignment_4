
try:
    user_input = input('Enter text to write to the file: ')
    file = open('output.txt','w')
    writing = file.write(user_input)
    file.close()
    print('Data successfully written to output.txt.')

except Exception as e:
    print('Exception while writing data :',e)

try:
    append_input = input('Enter additional text to append: ')
    file = open('output.txt','a')
    append = file.write('\n'+append_input)
    file.close()
    print('Data successfully appended')

except Exception as e:
    print('Exception while appending data :',e)

try:
    file = open('output.txt','r')
    reading = file.read()
    print('Final content of output.txt')
    print(reading)
    file.close()
except Exception as e:
    print('Exception while reading the data: ',e)