from itertools import cycle
import requests

# frequencies of english letters
frequencies = {'a': 0.0855, 'b': 0.0160, 'c': 0.0316, 'd': 0.0387, 'e': 0.1209,
               'f': 0.0218, 'g': 0.0209, 'h': 0.0496, 'i': 0.0732, 'j': 0.0022,
               'k': 0.0081, 'l': 0.0420, 'm': 0.0253, 'n': 0.0717, 'o': 0.0747,
               'p': 0.0206, 'q': 0.0010, 'r': 0.0633, 's': 0.0673, 't': 0.0894,
               'u': 0.0268, 'v': 0.0106, 'w': 0.0182, 'x': 0.0019, 'y': 0.0172,
               'z': 0.0011}

def error(candidate: bytes) -> float:
    l = len(candidate)
    score = 0
    for char, expected_freq in frequencies.items():
        freq = candidate.count(ord(char)) / l
        err = abs(freq - expected_freq)
        score += err
    return score

def xor_single(x:bytes, y:int):
    return bytes([xb^y for xb in x])

def best_xor_key(data: bytes) -> bytes:
    best_key = b''
    min_error = float('inf')
    for key in range(32, 128):
        candidate = xor_single(data, key)
        candidate_error = error(candidate)
        if candidate_error < min_error:
            best_key = key
            min_error = candidate_error
    return best_key

def repeating_xor(a: bytes, key) -> bytes:
    return bytes([x^y for (x,y) in zip(a,cycle(key))])
    

if __name__ == "__main__":
    file_url = 'https://projecteuler.net/resources/documents/0059_cipher.txt'
    ctxt = list(int(x) for x in requests.get(file_url).text.split(","))

    keysize = 3

    key = bytes([best_xor_key(ctxt[i::keysize]) for i in range(keysize)])
    print("\nKEY:\n",key.decode())

    message = repeating_xor(ctxt, key)
    print("\nMESSAGE:\n", message.decode('utf-8'))

    sol = sum(message)
    print("\nSOLUTION:\n", sol)
