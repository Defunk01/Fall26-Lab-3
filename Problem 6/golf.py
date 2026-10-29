"""
Complete the python code to determine Golf score from par and strokes using branching and print the Golf score.

Name:
Lab Time:
"""
def golf():
    par = int(input())
    strokes = int(input())

    if par < 3 or par > 5 or strokes < 1:
        print("Error")
        return

    diff = strokes - par

    if diff == -2:
        print("Eagle")
    elif diff == -1:
        print("Birdie")
    elif diff == 0:
        print("Par")
    elif diff == 1:
        print("Bogey")
    else:
        print("Error")


if __name__ == '__main__':
    golf()