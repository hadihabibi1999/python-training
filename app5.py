try:
    class Person :
        def __init__(self, age):
            self.age=age

    class Teenage(Person):
        def programmer(self):
             print('junior developer')
             return ''

    class Older(Person):
         pass


    print('''
             to fine out age of each person,
             type his name only :::....:::
             
             ''')

    name = input('name: ').lower()

    john = Person(25)
    hadi = Teenage(21)
    mosh = Older(32)

    age = vars()[name].age
    print(f'the age is: {age} years old')

    if name == 'hadi':

        print(hadi.programmer())

except KeyError :
    print('input name with letters only !')
