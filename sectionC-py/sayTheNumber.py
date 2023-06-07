# Function that inputs a number, and reads out the words of that number on the screen
def sayNumber(number):

    # Input validation
    if not isinstance(number, int):
        raise ValueError("Invalid input. Please provide an integer.")

    numberStr = str(number)
    length = len(numberStr)

    # Base Case
    if number < 0:
        return "No Number to Say!"

    # Arrays of the words of various numbers and their respective multiples/powers
    singleDigits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    doubleDigits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    multiplesOfTen = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    powers = ["hundred", "thousand", "million", "billion", "trillion"]

    # Single Digit Numbers
    if length == 1:
        return singleDigits[number]

    # Double Digit Numbers < 20
    if length == 2 and number < 20:
        num = number - 9
        return doubleDigits[num]

    # Double Digit Numbers >= 20
    if length == 2 and number >= 20:
        num1 = number // 10  # Integer division
        num2 = number % 10  # Modulo
        if num2 != 0:
            return multiplesOfTen[num1] + "-" + singleDigits[num2]
        else:
            return multiplesOfTen[num1]

    # Triple Digit Numbers
    if length == 3:
        num1 = number // 100  # Integer division
        num2 = number % 100  # Modulo
        if num2 != 0:
            return singleDigits[num1] + " " + powers[0] + " and " + sayNumber(num2)
        else:
            return singleDigits[num1] + " " + powers[0]

    # Numbers with Four or More Digits
    if length >= 4:
        power = (length - 1) // 3
        power_index = power if power <= 4 else 4
        num1 = number // (1000 ** power)  # Integer division
        num2 = number % (1000 ** power)  # Modulo
        if num2 != 0:
            separator = ' and ' if num2 < 100 else ', '
            return sayNumber(num1) + " " + powers[power_index] + separator + sayNumber(num2)
        else:
            return sayNumber(num1) + " " + powers[power_index]
