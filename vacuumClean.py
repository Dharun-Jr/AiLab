rooms = [True, False]
location = 0

while not all(rooms):
    print("Perceiving Room", chr(65 + location))

    if not rooms[location]:
        print("Cleaning Room", chr(65 + location))
        rooms[location] = True
    else:
        location = 1 - location
        print("Moving to Room", chr(65 + location))

print("All rooms are clean!")