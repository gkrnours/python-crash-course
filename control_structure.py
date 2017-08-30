words = []

# While loop. Run a block of code as long as a value is more or less true
# A value is more or less true if it's not None, False, 0, or something empty
word = input("type a word: ")
while word:
  words.append(word)
  word = input("type a word: ")

# if / elif / else structure.
# The elif and else are optionnal. Will run the first block of code following 
# a true-ish  value.
if len(words) == 0:
  print("You typed no words")
elif len(words) == 1:
  print("You typed one word")
else:
  print("you typed %s words" % len(words)
  
# for loop. Run a block of code with each value of a sequence.
# If words is a list with ["cat", "dog", "canary"], the block of code will run 
# three time, first with "cat"...
# Both while and for can be followed with an else. The block of code under the
# else will run if the block of code in the loop is not run at all.
for word in words:
  print("there is", len(word), "letters in", word)
else:
  print(":(")
