shift = -3 # defining the shift count

text = "outlook"

encryption = ""

for c in text:

        # find the position in 0-25
        c_unicode = ord(c)

        new_unicode=c_unicode+shift

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character
        
print("Plain text:",text)

print("Encrypted text:",encryption)