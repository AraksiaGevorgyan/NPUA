def roman_to_integer(s):
    roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    result = 0
    previous = 0

    for char in s:
        result+=roman[char]
        if roman[char] > previous:
            result -= 2*previous
        previous=roman[char]
    return result

roman_number = input("Roman number: ")
integer_number = roman_to_integer(roman_number)
print(f"The integer value  of '{roman_number}' is '{integer_number}' .")