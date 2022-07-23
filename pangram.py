def pang(string):
    """Return True if string is a pangram."""
    letter_set = set()
    for character in string.lower():
        if character.islower():
            letter_set.add(character)
    return len(letter_set) == 26


# or...

def pang2(string):
    """Return True if string is a pangram."""
    from string import ascii_lowercase

    # set-ify the lower case letters
    letter_set = set(ascii_lowercase)
    
    for character in string.lower():
        letter_set.discard(character)
    return len(letter_set) == 0
