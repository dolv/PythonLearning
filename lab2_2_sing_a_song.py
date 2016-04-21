import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

song = "Everybody sing a song:"
for i in range(0, y, 1):
    song += " "
    for j in range(0, x, 1):
        if j > 0:
            song += "-la"
        else:
            song += "la"
if z == 1:
    song += "!"
else:
    song += "."

print song
