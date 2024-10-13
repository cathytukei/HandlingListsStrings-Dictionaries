#Program 1
def alternate_cases(text):# Makes every other character uppercase and lowercase
  result = ""
  is_upper = True  # Start with uppercase
  for char in text:
    if char.isalpha():  # Check if the character is a letter
      result += char.upper() if is_upper else char.lower()
      is_upper = not is_upper  # Toggles case for next character
    else:
      result += char  # Add non-letter characters as is
  return result

text = "Hello World"
altered_text = alternate_cases(text)
print(altered_text)

#Program 2
def alternate_words(text): # Makes every other word uppercase and lowercase
  words = text.split() # splits the text into ondividual words
  result = [] # stores the modified words
  for i, word in enumerate(words):
    result.append(word.upper() if i % 2 == 0 else word.lower())
  return " ".join(result)

text = "I am learning to code"
altered_text = alternate_words(text)
print(altered_text) 


