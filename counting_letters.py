def letter_counter(string):
    string = string.lower()
    hashmap = {}

    # Counting every letter in the string. Adding them to the hashmap
    for letter in string:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1
    return hashmap


# Get the string from the user
s = input("Give me a string ")
print(letter_counter(s))
