"""
    Write a program that determines the fewest number of coins needed to make exact change.
    The program should then write out the amount of each coin to be used. 
    The coin denominations are dollars, quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent). 

Name:
Lab Time:
"""

def exact_change():
    input_val = int(input())

    if input_val <= 0:
        print("No change")
        return

    coins = [
        (100, "Dollar", "Dollars"),
        (25, "Quarter", "Quarters"),
        (10, "Dime", "Dimes"),
        (5, "Nickel", "Nickels"),
        (1, "Penny", "Pennies"),
    ]

    for value, singular, plural in coins:
        count = input_val // value
        input_val = input_val % value
        if count == 1:
            print(f"1 {singular}")
        elif count > 1:
            print(f"{count} {plural}")


if __name__ == '__main__':
    exact_change()