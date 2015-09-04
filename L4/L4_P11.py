def isVowel2(char):
  '''
  char: a single letter of any case
  returns: True if char is a vowel, False otherwise
  do use the keyword in
  '''

  vowels = ('a', 'e', 'i', 'o', 'u')
  if char.lower() in vowels:
    return True
  return False

print(isVowel2('B'))
