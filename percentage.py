"""This code finds the percentage of a given number(input) 
    out of a given whole(input).
"""

def percentage(): 
    value = float(input("Please enter the portion to be calculated: "))
    total = float(input("Please enter the total number: "))
    
    initial = (value/total)
    result = float(initial * 100)
    print(f"The percentage of the first number out of the whole"
        f"quantity is: {result} %. ")

percentage()




