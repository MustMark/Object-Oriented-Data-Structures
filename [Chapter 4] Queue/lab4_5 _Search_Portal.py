def check_map(width, height, room_map):
    if len(room_map) != int(height):
        return False
    else:
        for i in room_map:
            if len(i) != int(width):
                return False
    return True

width, height, room = input("Enter width, height, and room: ").split(" ")
room_map = room.split(",")
queue = []

if not check_map(width, height, room_map):
    print("Invalid map input.")