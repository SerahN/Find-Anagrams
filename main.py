# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

s1 = "name"
s2 = "mane"

def find_anagram(word, anagram):
    if(sorted(s1)==sorted(s2)):
     return True
    else:
      return False

print(find_anagram("name", "mane"))

