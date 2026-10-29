'''
 Complete the python code to find the smallest number among the three input numbers
 using branching and print the smallest number.

 Note: Please don't use python built-in functions to find the smallest number.

 Name: 
 Lab Time:
'''
def smallest_number():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if num1 <= num2 and num1 <= num3:
        print(num1)
    elif num2 <= num1 and num2 <= num3:
        print(num2)
    else:
        print(num3)

if __name__ == "__main__":
    smallest_number()