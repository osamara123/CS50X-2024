# TODO

while (True):
    try:
        height = int(input("Enter Height: "))
        if (height >= 1 and height <= 8):
            break
    except ValueError:
        print("Invalid input.")

# create mario
for i in range(1, height + 1, 1):
    for j in range(height, 0, -1):
        if j <= i:
            print("#", end='')
        else:
            print(" ", end='')
    print("\n", end='')
