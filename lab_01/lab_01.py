# 1
int_1 = int('1010', base=2)  # 10 w systemie binarnym
int_2 = int('2A', base=16)  # 42 w systemie szesnastkowym
float_1 = float('1.23')
float_2 = float(4)

print(f'Obiekt int_1: {int_1}, typ: {type(int_1)}')
print(f'Obiekt int_2: {int_2}, typ: {type(int_2)}')
print(f'Obiekt float_1: {float_1}, typ: {type(float_1)}')
print(f'Obiekt float_2: {float_2}, typ: {type(float_2)}\n')


# 2
for i in [int_1, int_2]:
    print(f'Liczba bitów w {i}: {int.bit_count(i)}')

for i in [float_1, float_2]:
    if float.is_integer(i):
        print(f'Liczba {i} jest liczbą całkowitą')
    else:
        print(f'Liczba {i} nie jest liczbą całkowitą')

# 3
def kalkulator_and(liczba_1, liczba_2):
    print(f'{liczba_1} AND {liczba_2} = {liczba_1 & liczba_2}')

def kalkulator_or(liczba_1, liczba_2):
    print(f'{liczba_1} OR {liczba_2} = {liczba_1 | liczba_2}')

def kalkulator_xor(liczba_1, liczba_2):
    print(f'{liczba_1} XOR {liczba_2} = {liczba_1 ^ liczba_2}')

def kty_bit(n, k):  # funkcja zwraca ktyBit liczby n
    return (n >> (k-1)) & 1;

print('')
kalkulator_and(10, 6)  # 1010 AND 0110 = 0010 = 2
kalkulator_or(10, 6)  # 1010 OR 0110 = 1110 = 14
kalkulator_xor(10, 6)  # 1010 XOR 0110 = 1100 = 12
print(kty_bit(int('1010', base=2), 1))
print(kty_bit(int('1010', base=2), 2))
print(kty_bit(int('1010', base=2), 3))
print(kty_bit(int('1010', base=2), 4))
