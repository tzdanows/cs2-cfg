import shutil

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
    "actual/anubis-t-spawns.cfg",
    "actual/anubis-t-spawns-hard.cfg",
    "actual/ancient-t-spawns.cfg",
    "actual/ancient-t-spawns-hard.cfg",
    "actual/ancient-ct-spawns.cfg",
    "actual/ancient-ct.cfg",
    "actual/ancient-ct-hard.cfg",
    "actual/mirage-t-spawns.cfg",
    "actual/mirage-t-spawns-hard.cfg",
    "actual/surf.cfg",
]

# put your path here
cs2_destination = [
    r"D:\SteamLibrary\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg"
]

for cfg in cs2_files_to_copy:
    for dest in cs2_destination:
        print("Copying from {} to {}".format(cfg, dest))
        shutil.copy(cfg, dest)
