def rotate_90(lines):
    if len(lines) == 0:
        return []
    rotated = []
    for col in range(len(lines[0])):
        new_line = ""
        for row in range(len(lines) - 1, -1, -1):
            new_line += lines[row][col]
        rotated.append(new_line)
    return rotated

def read_art(file_name):
    with open(file_name, "r") as my_file:
        content = my_file.readlines()

    for i in range(len(content)):
        content[i] = content[i].rstrip("\n")
    if not content:
        return []
    return content

def rotate(lines, degrees):
    while degrees > 0:
        lines = rotate_90(lines)
        degrees -= 90
    return lines


def ask_degrees():
    degrees = input("how many degrees to rotate")
    return int(degrees)

def ask_file_name():
    file_name = input("enter name file")
    return file_name



def main():
    file = ask_file_name()
    picture = read_art(file)
    degrees = ask_degrees()
    picture = rotate(picture, degrees)
    for line in picture:
        print(line)

if __name__ == "__main__":
    main()

