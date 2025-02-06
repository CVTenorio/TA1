#Program 1
def count_alphabets(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    total_vowels = 0
    total_consonant = 0
    total_spaces = 0
    total_other_chars = 0
    for char in string:
        if char in vowels:
            total_vowels += 1
        elif char in consonants:
            total_consonant += 1
        elif char == " ":
            total_spaces += 1
        else:
            total_other_chars += 1
    print(f"total number of Vowels: {total_vowels}")
    print(f"total number of Consonants: {total_consonant}")
    print(f"total number of Spaces: {total_spaces}")
    print(f"total number of Other Characters: {total_other_chars}")
input_string = input ("Enter a word: ")
count_alphabets(input_string)