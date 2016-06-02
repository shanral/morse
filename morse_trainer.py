import sys

LETTER_TO_CODE = {
    'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',
    'f': '..-.', 'g': '--.',  'h': '....', 'i': '..',   'j': '.---',
    'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',   'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',
    'u': '..-',  'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--',
    'z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    ' ': '     '
    }

# create the reverse of the above
CODE_TO_LETTER = {v: k for k, v in LETTER_TO_CODE.items()}

def verify_message(msg):
    keys = LETTER_TO_CODE.keys()
    for char in msg:
        if char not in keys and char != ' ':
            sys.exit('Error, invalid character: ' + char)

# TODO: sub all \s{5} to \s{1}, verify as normal
#def verify_morse(msg):
#    sub_out_5_spaces_to_1
#    for char in msg:
#        if char != '.' or char != '-':
#            sys.exit('Error, invalid character: ' + char)

# BUG: handles spaces incorrectly
#  possible poor solution, change length of space in dict, but would cause
#  problems if there are leading or trailing spaces in the message, need
#  something else
def print_morse(msg):
    verify_message(msg)
    chars = list(msg)
    output = ''
    output = output + ' '.join([LETTER_TO_CODE[x] for x in chars])
    return output

def print_words(msg):
    #verify_morse(msg)
    output = ''

    words = msg.split(' ' * 5)
    for word in words:
        chars = word.split(' ')
        output = output + ''.join([CODE_TO_LETTER[x] for x in chars]) + ' '

    # TODO: current process will have a trailing space, can we fix this?
    return output.strip()

print print_morse('time fact')
print print_words('- .. -- .     . -- . -')
