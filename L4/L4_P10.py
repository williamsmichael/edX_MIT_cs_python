def isVowel(char):
  '''
  char: a single letter of any case
  returns: True if char is a vowel and False otherwise
  cannot use the keyword 'in'
  '''
  if (char.lower() == 'a' or
      char.lower() == 'e' or
      char.lower() == 'i' or
      char.lower() == 'o' or
      char.lower() == 'u' or
      char.lower() == 'e'):
      return True
  return False

print(isVowel('B'))

# source: http://stackoverflow.com/questions/14667578/check-if-a-number-already-exist-in-a-list-in-python
