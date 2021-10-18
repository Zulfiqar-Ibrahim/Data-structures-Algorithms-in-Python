string = "Hello World, my name is Zulfiqar Ibrahim"

print(string)

for i in range (0, len(string)):
    letter = string[i]
    #print(letter)
    
print(len(string))
print(string.count('a'))
print(string[string.find("a")])
print(string.index('Zulfiqar'))
print(string.count(' '))

print(string[:5])
print(string[6:20])
print(string[-7:])


print(string.startswith('H'))
print(string.endswith('m'))
print(string.upper())
print(string.lower())

split_string = string.split(' ')
print(split_string)


new_list = []
for word in split_string:
    first_letter = word[0]
    first_letter_upper = first_letter.upper()
    new_word = word.replace(first_letter,first_letter_upper)
    new_list.append(new_word)
    
new_string = ' '.join(str(word) for word in new_list)
print(new_string)


   
