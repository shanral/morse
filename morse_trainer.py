CODE = {
    'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',
    'f': '..-.', 'g': '--.',  'h': '....', 'i': '..',   'j': '.---',
    'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',   'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '---',  't': '.',
    'u': '..-',  'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--',
    'z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

print CODE['a']

def valid_morse(char):
    if char not in CODE and char != ' ':
        sys.exit('Error, invalid character: ' + char)
    else:
        return True

def print_morse(string):
    for char in string:
        if valid_morse(char):
            print CODE[char]

print_morse('test')
