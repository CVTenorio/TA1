#Program 3

def a_For(rows):
    for x in range (1, rows + 1):
        for o in range(1, x + 1):
            print("*", end =" ")
        print()
        
def b_While(rows):
    x = 1
    while x <= rows:
        y = 1
        while y <= x:
            print("*", end = " ")
            y += 1
        print()
        x += 1            
options = {
    "a": a_For,
    "b": b_While
}

choice = input("Enter 'a or A' for for-loop or 'b or B' for while-loop: ").strip().lower()

if choice in options:
    rows = int(input ("Enter number of rows: "))
    options[choice](rows)
else:
    print ("Invalid choice! Try Again")