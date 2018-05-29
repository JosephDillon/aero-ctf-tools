import argparse
import caesar
import morse
parser = argparse.ArgumentParser(prog='Aero CTF Tools')
subparsers = parser.add_subparsers()

print(caesar.decipher('test', 13))
print(morse.encode('ABC'))
encodedMorse = morse.encode('ABC')
print(morse.decode(encodedMorse))
