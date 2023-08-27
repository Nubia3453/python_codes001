#escsape chars are used to cut/delimit the strings.

#    \t = tab delimiter - inserts 8 char space befor the string
print('\t "this is tabbed string"')

#    \n = new line - put the part of string on new line.
print('"this line will contine to" \n"newline"')









print('C:\Program Files\Internet Explorer\SIGNUP')


#issue with tabbed and new line escape char.
print('C:\Program Files\newfolder\SIGNUP\text.txt')
#here the issue is that the \n and \t are part of string itself and considered as escape char.

print('C:\\Program Files\\newfolder\\SIGNUP\\text.txt')

print(r'C:\Program Files\newfolder\SIGNUP\text.txt')