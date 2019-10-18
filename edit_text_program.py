lines = []
with open(r"snake.txt", "r") as file:
    for line in file:
#        line[-4:]
        print (line [4:])
        lines += line [4:]
#    lines = file.readlines()
#del lines[1]
with open(r"snake_edit.txt", "w") as file:
    file.writelines(lines)