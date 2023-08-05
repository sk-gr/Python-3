def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

print(letter_check("strawberry", "o"))

def contains(big_string, little_string):
  if little_string in big_string:
    return True
  return False

def common_letters(string_one, string_two):
  common =[]
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
