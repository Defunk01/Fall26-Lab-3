'''
    Complete the python code to determine the direction of the interstate highway from the number
    using branching and print the direction of the interstate highway. Additionally, if the highway 
    is auxiliary, print the number of the primary highway it serves. 
    If the number is not a valid interstate highway number, print an error message.

Name:
Lab Time:
'''
def interstate():
    highway_number = int(input())

    if highway_number < 1 or highway_number > 999:
        print(f"{highway_number} is not a valid interstate highway number.")

    elif highway_number <= 99:
        direction = "east/west" if highway_number % 2 == 0 else "north/south"
        print(f"I-{highway_number} is primary, going {direction}.")

    else:
        primary = highway_number % 100

        if primary == 0:
            print(f"{highway_number} is not a valid interstate highway number.")
        else:
            direction = "east/west" if primary % 2 == 0 else "north/south"
            print(f"I-{highway_number} is auxiliary, serving I-{primary}, going {direction}.")

if __name__ == "__main__":
    interstate()