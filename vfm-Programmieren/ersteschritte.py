# Jetzt wollen wir alle Quadratzahlen bis zur eingegebenen Zahl berechnen.

text = "Thqr! Qvrfrf Cebtenzz shaxgvbavreg haq irefpuyüffryg/ragfpuyüffryg qra Grkg!"

def rot13(text):
    d = {}
    for ascii_code in (65, 97):
        for alphabet_index in range(26):
            d[chr(ascii_code + alphabet_index)] = \
            chr(ascii_code + (alphabet_index + 13) % 26)
    out = ''.join([d.get(letter, letter) for letter in text])
    return out

print(rot13(text))