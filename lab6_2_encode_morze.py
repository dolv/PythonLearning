def encode_morze(text):
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--.."
    }
    signal = {
        '.': '^_',
        '-': '^^^_'
    }
    morse_str = ''
    for letter in text.upper().strip():
        if letter in morse_code.keys():
            for char in morse_code[letter]:
                morse_str += signal[char]
            morse_str += '__'
        if letter == ' ':
            morse_str += "____"

    return [morse_str, morse_str[:-3]][len(morse_str) > 0]
print encode_morze('')