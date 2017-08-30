# Simple values. Really simple. True, False, None. 
# First two are the result of test, like 18 < age. Third one is for lack of value.
adult = True
rich = False
cakes_on_the_table = None

# Number. Can be really simple
age = 27
height = 5.7
# Can also be more complex, if you need math
year_of_birth = 1.99e3
# Or plain crazy, if you need math
polar_coordinate = 3 + .7j
# All of these are of limited precision. 
# Good enough for sending rocket on mars, not for tax return. Go figure...

# Word are string of character. Or simply string.
name = "Louise Alice"
# Like all sequence, we can count how long they are and take a letter or a slice
####~####~####~####*####~####~####~####*####~####~####~####*####~####~####~####*
name_length = len(name)
initial = name[0]
first_name = name[0:6]
second_name = name[-5:]
# Slice take a beginning value and an end value. 
# Missing values are replaced with beginning or end. Whatever make sense.

# List are a list of value. They have an order. The values can be mixed, like
# a number, then a string, then four True, then a list, then three number...
names = name.split()
2 == len(names)
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21]

# Dict are list of key/value couple. Make it easy to get a value
me = {"name":"Louise", "age":27, "height":5.7}
me["age"] == 27
