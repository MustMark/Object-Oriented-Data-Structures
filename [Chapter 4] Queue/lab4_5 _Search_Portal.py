def check_map(width, height, room_map):
    check_F = False
    if len(room_map) != int(height):
        return False
    else:
        for i in room_map:
            if len(i) != int(width):
                return False
            if "F" in i:
                check_F = True
    return check_F

def look_map(room_map, location):
    queue = []
    if location[1] != 0 and room_map[location[1] - 1][location[0]] == "_":
        queue.append((location[0], location[1] - 1))
    if location[0] != len(room_map[location[1]]) - 1 and room_map[location[1]][location[0] + 1] == "_":
        queue.append((location[0] + 1, location[1]))
    if location[1] != len(room_map) - 1 and room_map[location[1] + 1][location[0]] == "_":
        queue.append((location[0], location[1] + 1))
    if location[0] != 0 and room_map[location[1]][location[0] - 1] == "_":
        queue.append((location[0] - 1, location[1]))

    if location[1] != 0 and room_map[location[1] - 1][location[0]] == "O":
        return "Found the exit portal."
    if location[0] != len(room_map[location[1]]) - 1 and room_map[location[1]][location[0] + 1] == "O":
        return "Found the exit portal."
    if location[1] != len(room_map) - 1 and room_map[location[1] + 1][location[0]] == "O":
        return "Found the exit portal."
    if location[0] != 0 and room_map[location[1]][location[0] - 1] == "O":
        return "Found the exit portal."
    return queue

def get_location(room_map):
    for y in range(len(room_map)):
        for x in range(len(room_map[y])):
            if room_map[y][x] == "F":
                return (x, y)
                
width, height, room = input("Enter width, height, and room: ").split(" ")
room_map = room.split(",")
queue = []

if not check_map(width, height, room_map):
    print("Invalid map input.")
else:
    queue.append(get_location(room_map))
    while queue:
        print(f"Queue: {queue}")
        x, y = queue.pop(0)
        room_map[y] = room_map[y][0:x] + "F" + room_map[y][x+1:]
        look_map_result = look_map(room_map, (x, y))
        if look_map_result == "Found the exit portal.":
            print("Found the exit portal.")
            break
        else:
            queue.extend(i for i in look_map_result if i not in queue)
        x, y = get_location(room_map)
        room_map[y] = room_map[y][0:x] + "X" + room_map[y][x+1:]
        if not queue:
            print("Cannot reach the exit portal.")