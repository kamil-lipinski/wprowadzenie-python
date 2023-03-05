# Padding and aligning strings - print('{:>10}'.format('test'))
print(f'{"test":>10}')

# Truncating long strings - print('{:.5}'.format('xylophone'))
print(f'{"xylophone":.5}')

# Named placeholders - print('{first} {last}'.format(first='Hodor', last='Hodor!'))
first = 'Hodor'
last = 'Hodor!'
print(f'{first} {last}')

# Getitem and Getattr - print('{p[first]} {p[last]}'.format(p=person))
person = {'first': 'Jean-Luc', 'last': 'Picard'}
print(f'{person["first"]} {person["last"]}')

# Parametrized formats - print('{:{align}{width}}'.format('test', align='^', width='10'))
print(f'{"test":{"^"}10}')

