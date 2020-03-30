dictionary = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
}
list = ()
list = input('> ')
list.split(',')
output = ''
for num in list:
    output+=dictionary.get(num,'!')+', '
print(output)
