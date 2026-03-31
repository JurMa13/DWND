x = 5
y = 5
# Počáteční pozice

while True:
    print("Player position:", x, y)
    move = input("Move (w=up, s=down, a=left, d=right, q=quit): ")

# Posunutí o jeden pixel
    if move == "w":
        y = y - 1
    elif move == "s":
        y = y + 1
    elif move == "a":
        x = x - 1
    elif move == "d":
        x = x + 1
    elif move == "q":
        print("Game Over!")
        break
    else:
        print("Invalid input!")

    # Na hranice mapy
    if x < 0:
        x = 0
    if x > 10:
        x = 10
    if y < 0:
        y = 0
    if y > 10:
        y = 10