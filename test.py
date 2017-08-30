# Test are used to turn more than one value into a True or False value
# It's used in control structure, to know what the code should do.

# When you have a single value, it have an implicit truth value.
# It's sometime said these value are trueish or falseish.
# All the following values are falseish
False
None
0
0.
0e1
""
[]
()
{}
# Pretty much everything else is Trueish.

# With two or more values, comparison are available.
from random import randint
age = randint(10, 30)
major = 18 <= age
teenage = 12 < age < 18
# Most of the comparision operator are the same as other language.
# == and != for equality and difference
# <, <=, >, >= for which value is bigger.
# Work well with number, work with string, don't work with both

# These comparison produce True or False. These can be combined
# Unlike most programming language, python use plain english keyword
minor = not major
me = age == 27 and name == "Louise"
cool_color = color == "pink" or color == "blue"
