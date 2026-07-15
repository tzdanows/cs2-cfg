import os
import shutil

cs2_files_to_copy = [
    "actual/nades.cfg",
    "actual/settings.cfg",
    "actual/autoexec.cfg",
    "actual/vs.cfg",
    "actual/awp.cfg",
    "actual/pistol.cfg",
    "actual/rifle.cfg",
    "actual/dm.cfg",
    "actual/dm2.cfg",
]

STEAM_USERDATA = r"C:\Program Files (x86)\Steam\userdata"
GAME_CFG_DIRS = [
    r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg",
]

def discover_cfg_dirs():
    dirs = list(GAME_CFG_DIRS)
    if not os.path.isdir(STEAM_USERDATA):
        print(f"Warning: Steam userdata not found at {STEAM_USERDATA}")
        return dirs
    for steamid in os.listdir(STEAM_USERDATA):
        cfg_path = os.path.join(STEAM_USERDATA, steamid, "730", "local", "cfg")
        if os.path.isdir(cfg_path):
            dirs.append(cfg_path)
    return dirs

cs2_destination = discover_cfg_dirs()
print(f"Found {len(cs2_destination)} destination(s):")
for d in cs2_destination:
    print(f"  {d}")
print()

errors = []
for cfg in cs2_files_to_copy:
    for dest in cs2_destination:
        try:
            shutil.copy(cfg, dest)
            print(f"Copied {cfg} -> {dest}")
        except Exception as e:
            errors.append((cfg, dest, e))
            print(f"FAILED {cfg} -> {dest}: {e}")

if errors:
    print(f"\n{len(errors)} error(s) occurred.")
else:
    print("\nAll files copied successfully.")
