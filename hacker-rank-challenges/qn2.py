# Detect Floating Point Number
# You are given a string N.
# Your task is to verify that N is a floating point number.

# In this task, a valid float number must satisfy all of the following requirements:

#  Number can start with +, - or . symbol.
# For example:
# ✔ +4.50
# ✔ -1.0
# ✔ .5
# ✔ -.7
# ✔ +.4
# ✖  -+4.5

# Number must contain at least 1 decimal value.
# For example:
# ✖ 12.
# ✔ 12.0

# Number must have exactly one . symbol.
# Number must not give any exceptions when converted using float(N).

# Input Format

# The first line contains an integer T, the number of test cases.
# The next T line(s) contains a string .

import re
T = int(input())
for _ in range(0, T):
    matchObj = re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())
    print(bool(matchObj))
