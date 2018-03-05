#!/bin/python3

import sys

def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for c in range(0, len(s)):
        lo = s[c].lower()
        if lo in alphabet:
            index = (k + alphabet.find(lo)) % 26
            char = alphabet[index]
            encrypted += (char if s[c].islower() else char.upper())
        else: encrypted += s[c]
    return encrypted

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
