def world_size(size):
    intl_size = {
        'XXS': {
            'GER': 36,
            'US': 8,
            'FR': 38,
            'GB': 24
        },
        'XS': {
            'GER': 38,
            'US': 10,
            'FR': 40,
            'GB': 26,
        },
        'S': {
            'GER': 40,
            'US': 12,
            'FR': 42,
            'GB': 28,
        },
        'M': {
            'GER': 42,
            'US': 14,
            'FR': 44,
            'GB': 30,
        },
        'L': {
            'GER': 44,
            'US': 16,
            'FR': 46,
            'GB': 32,
        },
        'XL': {
            'GER': 46,
            'US': 18,
            'FR': 48,
            'GB': 34,
        },
        'XXL': {
            'GER': 48,
            'US': 20,
            'FR': 50,
            'GB': 36,
        },
        'XXXL': {
            'GER': 50,
            'US': 22,
            'FR': 52,
            'GB': 38,
        },
    }
    return intl_size.get(size).items()


print("""'Калькулятор размеров женского белья'\n
Размер необходимо вводить в международном формате
(пример: s, xs, xl ....)\n""")

size = input('Введите размер:').upper()
print()

while size not in 'XXS,XS,S,M,L,XL,XXL,XXXL':
    size = input('ERROR\nВведите корректный размер:').upper()
    print()

print('Международному размеру {} '
      'соответствуют следующие размеры:\n'.format(size))

for nation, size in world_size(size):
    print('{:3} ==> {}'.format(nation, size))




