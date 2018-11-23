x = float(input("Enter number2: "))

if 0 < x < 7:
        print("Value in range, let's continue")
        y = 2 * x - 5
        if (y > 0):
            print("y is possitive")
        else:
            if (y < 0):
                print("y is negative")
            else:
                print("y is 0")
