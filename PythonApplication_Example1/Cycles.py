x = float(input("Enter number: "))

if (0 < x < 7):
    print("It's normal.Continiue...")
    y = 2 * x - 5
    if (y > 0):
        print("y greater then 0")
    elif (y < 0):
        print("y smaller then 0")
    else:
         print("y is 0")
           