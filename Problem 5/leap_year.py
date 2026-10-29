"""
    Complete the following python code to determine if the year entered by the user is a leap year.

Name:
Lab Time:
"""

def leap_year():
    is_leap_year = False
    input_year = int(input())

    if input_year % 400 == 0:
        is_leap_year = True
    elif input_year % 100 == 0:
        is_leap_year = False
    elif input_year % 4 == 0:
        is_leap_year = True

    if is_leap_year:
        print(f"{input_year} - leap year")
    else:
        print(f"{input_year} - not a leap year")


if __name__ == '__main__':
    leap_year()