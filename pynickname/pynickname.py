import random
import re

def pynickname(name):

     # Extract the first name from the input
     first_name = name.split()[0]

     # Check that the first name contains only letters and whitespace
     if not re.match(r'^[a-zA-Z ]+$', first_name):
         return None

     nicknames = [first_name]

     # add augmentative
     last_consonant = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+', first_name)[-1]
     vowel = re.findall(r'[aeiouAEIOU]', first_name[first_name.index(last_consonant):] + "a")[0]
     nicknames.append(first_name[:first_name.index(vowel)] + vowel + last_consonant + "ão")

     # add diminutive
     last_consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+', first_name)[-2:]
     if last_consonants:
         vowel = re.findall(r'[aeiouAEIOU]', first_name[first_name.index(last_consonants[-1]):] + "a")[0]
         nicknames.append(first_name[:first_name.index(vowel)] + vowel + last_consonants[-1] + "inho")

     # Add gender inversion
     if first_name[-1] in "aeiouAEIOU":
         if first_name[-1] in "aA":
             nicknames.append(first_name[:-1] + "o")
         else:
             nicknames.append(first_name[:-1] + "a")
     else:
         if first_name[-2:] in ["no", "No"]:
             nicknames.append(first_name[:-2] + "na")
         else:
             nicknames.append(first_name[:-1] + "a")

     # Add name shortening
     shorten = first_name
     while not re.findall(r'[aeiouAEIOU]$', reduction):
         reduction = reduction[:-1]
     nicknames.append(reduce)

     # Add name pun
     if first_name[-1] == "o":
         nicknames.append(first_name[:-1] + "oca")
     else:
         nicknames.append(first_name + "zinha")

     # Pick a random nickname from the list
     nickname = random.choice(nicknames)

     return nickname

nickname = pynickname("Francisco")
print(nickname)