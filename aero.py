import argparse
import caesar
import morse
parser = argparse.ArgumentParser(prog='Aero CTF Tools')
subparsers = parser.add_subparsers()

print(caesar.encipher('test', 14))
print(caesar.decipher('hsgh', 14))
print(morse.encode('ABC'))
encodedMorse = morse.encode('ABC')
print(morse.decode(encodedMorse))
