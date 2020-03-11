
count = 0
while count <= 4 :
    weight = float(input('weight: '))
    l_or_k = input('(L)bs or (K)g ? ')

    if l_or_k.lower() == 'l':
       weight *= 0.45
       print(f'your weight {weight} kilograms')
    elif l_or_k.lower() == 'k':
        weight /=  0.45
        print(f'your weight {weight} pounds')
    else:
        print('something were wrong...')

