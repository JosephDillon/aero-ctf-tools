import argparse

from venv.ciphers import *
from venv.analysis import *
from venv.tests import *


parser = argparse.ArgumentParser(prog='Aero CTF Tools')
parser.add_argument('-e', '--encrypt', action='store_true')
parser.add_argument('-d', '--decrypt', action='store_true')
parser.add_argument('-a', '--analyze', action='store_true')
parser.add_argument('--caesar', action='store_true')
parser.add_argument('--morse', action='store_true')
parser.add_argument('--atbash', action='store_true')
parser.add_argument('--frequency', action='store_true')


