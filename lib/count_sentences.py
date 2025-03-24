#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value =""):
    self._value = ""
    self.value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if type(new_value) == str:
      self._value = new_value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    last_character = self.value[-1]
    if last_character == ".":
      return True
    else:
      return False
  
  def is_question(self):
    last_character = self.value[-1]
    if last_character == "?":
      return True
    else:
      return False
  
  def is_exclamation(self):
    last_character = self.value[-1]
    if last_character == "!":
      return True
    else:
      return False
  
  def count_sentences(self):
    sentence_count = re.findall(r'[^.!?]+[.!?]', self.value)
    return len(sentence_count)
  
    # sentence_count = 0
    # for char in self.value:
    #   if char == "." or char == "?" or char == "!":
    #     sentence_count = sentence_count + 1
    # return sentence_count
   
  # import re
# Example:
# text = "The cat and the hat are on the mat."
# pattern = r"at"

# result = re.findall(pattern, text)
# print(result)  # Output: ['at', 'at', 'at']

# text = "My phone number is 123-456-7890 and my friend's is 987-654-3210."
# pattern = r"(\d{3})-(\d{3})-(\d{4})"

# result = re.findall(pattern, text)
# print(result)
# # Output: [('123', '456', '7890'), ('987', '654', '3210')]

  
    