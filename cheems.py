import random



def cheems(str):
    str_list = list(str)
    random_index = random.randint(1, len(str))
    str_list.insert(random_index, 'm')
    cheems_str = ''.join(str_list)
    return cheems_str
   
re = 'Y'
while re.upper() != 'N':
    user_input = input('Enter a word to cheematize: ')
    out = cheems(user_input)
    print('Cheems says {}'.format(out))
    re = input('wanna run again?(Y/N): ')
