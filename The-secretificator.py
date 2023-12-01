#hashing and dehashing functions by jojo:
hashing_dict = {
    'A': '+',
    'B': 'Б',
    'C': '*',
    'D': 'Г',
    'E': 'Д',
    'F': '^',
    'G': 'Ё',
    'H': 'Ж',
    'I': '@',
    'J': 'И',
    'K': 'Й',
    'L': ')',
    'M': 'Л',
    'N': '#',
    'O': '/',
    'P': '<',
    'Q': 'П',
    'R': '.',
    'S': '?',
    'T': '!',
    'U': '~',
    'V': 'Ф',
    'W': '`',
    'X': 'Ц',
    'Y': 'Ч',
    'Z': 'Ш',
    'a': '$',
    'b': ':',
    'c': 'в',
    'd': '>',
    'e': 'д',
    'f': '&',
    'g': 'ё',
    'h': 'ж',
    'i': 'з',
    'j': 'и',
    'k': 'й',
    'l': 'к',
    'm': 'л',
    'n': 'м',
    'o': 'н',
    'p': '%',
    'q': 'п',
    'r': '=',
    's': '_',
    't': 'т',
    'u': 'く',
    'v': 'ф',
    'w': '}',
    'x': 'ц',
    'y': 'ч',
    'z': 'ш',
    ' ': '|',
    '0': 'れ',
    '1': 'い',
    '2': 'に',
    '3': 'さ',
    '4': 'し',
    '5': 'ご',
    '6': 'ろ',
    '7': 'ち',
    '8': 'は',
    '9': 'う',
    ',':','
}

def hasher(string):
    for key in hashing_dict:
        string = string.replace(key, hashing_dict[key])
    return string
def dehasher(string):
    for key in hashing_dict:
        string = string.replace(hashing_dict[key], key)
    return string

while True:
    print('Hello to encryption hacker center by jojo')
    print('please choose an option(1|2):')
    print('1- Encrypt#')
    print('2-Dencrypt!#')
    choice = input('Enter Choice : ')
    message = input('Enter the message@ : ')
    if choice == '1':
        print(hasher(message))
        break
        
    elif choice == '2':
        print(dehasher(message))
        break
    else:
        print('Sorry, Invalid Input!, please try again')
