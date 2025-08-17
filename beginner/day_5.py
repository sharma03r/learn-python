import random
# Alphabets (A-Z and a-z)
alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

# Numbers (0-9)
numbers = [str(i) for i in range(10)]

# Special Characters (Common ASCII punctuation characters)
special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/'
]
combined_list = [alphabets, numbers, special_characters]
len_of_password = int(input("What is the preffered length of the password?"))
i=0
password = ""
while i<len_of_password:
  list_selected = random.randint(0,len(combined_list)-1)
  character_selected = random.randint(0, len(combined_list[list_selected])-1)
  password += combined_list[list_selected][character_selected]
  i+=1

print(password)