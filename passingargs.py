# First script

import sys
import argparse

# print(sys.platform)

# x = 'Spam!'
# print(x * 8)

# Passing arguments to python scripts

def get_sum_of_args(num1, num2, num3):
    return (int(num1) + int(num2) + int(num3))

# Option 1 - Through sys module
# num1 = sys.argv[1]
# num2 = sys.argv[2]
# num3 = sys.argv[3]
# print(get_sum_of_args(num1, num2, num3))

# Option 2 - Argparse module
parser = argparse.ArgumentParser(
    description="Script that adds 3 numbers from CMD"
)

parser.add_argument("--num1", required=True, type=int)
parser.add_argument("--num2", required=True, type=int)
parser.add_argument("--num3", required=True, type=int)
args = parser.parse_args()

print(get_sum_of_args(args.num1, args.num2, args.num3))