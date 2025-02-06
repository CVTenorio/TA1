#Program 2

def SumOfDigits (string):
    temp = "0"
    total = 0
    for char in string:
        if (char.isdigit()):
            temp += char
        else:
            total += int(temp)
            temp = "0"
    return total + int(temp)

Word = input ("Enter a String: ")
print ("Sum of digits from string: ", SumOfDigits(Word))