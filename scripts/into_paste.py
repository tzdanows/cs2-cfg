binds = []

config = "config.cfg"
autoexec = "autoexec.cfg"

with open(config, 'r') as fp:
    for line in fp.readlines():
        line = line.strip()
        binds.append(line)

paste = ""

ctr = 0
for bind in binds:
    paste += " {} ;".format(bind)
    if ctr % 8 == 0:
        paste += "\n\n"
    ctr += 1

text_file = open("paste.txt", "w")
n = text_file.write(paste)
text_file.close()
