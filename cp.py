import shutil

csgo_files_to_copy = [
    "actual/nades.cfg",
    "actual/config.cfg",
    "actual/autoexec.cfg",
    "actual/video.txt",
    "actual/vs.cfg",
    "actual/awp.cfg",
    "actual/pistol.cfg",
    "actual/rifle.cfg",
]

cs2_files_to_copy = [
    "actual/nades.cfg",
    "actual/cs2.cfg",
    "actual/autoexec.cfg",
    "actual/video.txt",
    "actual/vs.cfg",
    "actual/awp.cfg",
    "actual/pistol.cfg",
    "actual/rifle.cfg",
    "actual/cs2.cfg",
]

destinations = [
    r"D:\Downloads\userdata\848999781\730\local\cfg",
    r"D:\Downloads\userdata\115874183\730\local\cfg",
    r"C:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg"
]

cs2_destination = [
    r"C:\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg"
]

for cfg in csgo_files_to_copy:
    for dest in destinations:
        print("Copying from {} to {}".format(cfg, dest))
        shutil.copy(cfg, dest)

for cfg in cs2_files_to_copy:
    for dest in cs2_destination:
        print("Copying from {} to {}".format(cfg, dest))
        shutil.copy(cfg, dest)
