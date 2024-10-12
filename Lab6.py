

english = "abcdefghijklmnopqrstuvwxyz "

def stupid_frenchman_square(alphabet):
    n = len(alphabet)
    for i in range(n):
        print(f'{alphabet[i]}', end='|')
    print()
    for i in range(n):
        print('-', end='|')
    print()
    for i in range(n):
        print(loopfromindex(alphabet,i))


def loopfromindex(index, i):
    n = len(index)
    result = ' '
    for _ in range(n):
        result += index[i % n]
        print(index[i % n] + '|', end=" ")
        i += 1
    return result

def lettertoindex(letter, alphabet):
    letter = letter.lower()
    for i, l in enumerate(alphabet.lower()):
        if l == letter:
            return i

def indextoletter(alphabet, index):
    i = 0
    for l in alphabet:
        if i == index:
            return l
        i += 1

def frenchmen_index(key_letter, plaintext_letter, alphabet):
    n = len(alphabet)
    k_i = lettertoindex(key_letter, alphabet)
    p_i = lettertoindex(plaintext_letter, alphabet)
    cipher_index = ((k_i + p_i) % n)
    cipher_letter = indextoletter(alphabet, cipher_index)
    return cipher_letter

def frenchmen_encryption(keytext, plaintext, alphabet):
    r = ' '
    n = len(plaintext)
    m = len(keytext)
    for i in range(n):
       r += frenchmen_index(keytext[i % m], plaintext[i], alphabet)
    return r












#stupid_frenchman_square(english)
#print(lettertoindex('q', english))
#print(indextoletter(english, 21))

#print(frenchmen_index('t','u',english))
print(frenchmen_encryption(input("What is your Keytext?"), input("What message are you encrypting?"), english))

