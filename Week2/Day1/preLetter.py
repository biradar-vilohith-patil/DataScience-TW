def preLetterCase(string , letter):
    string=string.lower()
    a = string.find(letter)
    if a==-1:
        return string
    
    first = string[0:a].lower()
    sec = string[a : len(string)].upper()
    return first+sec

print(preLetterCase("CAtCHa","a"))
print(preLetterCase("Preteen","e"))
print(preLetterCase("You've got this","m"))
print(preLetterCase("Keep trying","k"))

