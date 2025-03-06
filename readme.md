# CS2 config
1. Clone this repository
2. Edit your config in the `actual/config.cfg` and `actual/autoexec.cfg` to match your  requirements
3. Match your config filepaths in `cp.py` with the defaults associated to the game cfg filepath (mine is an example)
4. Execute cp.py and it should copy/paste your cfg into the corresponding folders

# Launch Options 
to navigate: right click cs2 in steam library, properties, launch options at the bottom of the price
### CS2: 
```
-novid -freq 240 -w 1440 -h 1080 -tickrate 128 -fullscreen -nojoy +exec config.cfg
```
OR exec in the game console with `exec config.cfg`


# Video Settings:

Resolution: 1280 x 960 stretched OR 1440 x 1080 stretched

[Video settings here](https://github.com/tzdanows/cs2-cfg/blob/main/actual/cs2_video.txt)

# Contributing Guidelines:

* Contributions are always welcome to the `profigs` and `playerfigs` folders if you'd like to add more configs
* However please do not modify any other folders and follow the `config.cfg` naming convention with `[playername] folders
* Forks are always welcome for personal use
* Overrides of pro configs are welcome especially if outdated heavily

### make changes then run
```bash
git add . ; git commit -m "cfg change" ; git push ; python .\cp.py
```

# Extra

## NVIDIA Control Panel
* Digital Vibrance: 80% or 50%(default)
* [3D Settings](https://i.imgur.com/vs5EpQx.gif) (potentially not optimal)
* Change Resolution --> 1920 x 1080(native) @ 360hz
    * ensure your res is available in nvidia control panel
* Adjust Desktop Size and Position --> Full-Screen
## Enable Hypervisor 
```
bcdedit /set hypervisorlaunchtype auto  
```

### Disable Hypervisor  
```
bcdedit /set hypervisorlaunchtype off  
```

## Follow these configuration tips:

* [https://wiki.refrag.gg/en/pc-optimization-increase-fps-csgo](https://wiki.refrag.gg/en/pc-optimization-increase-fps-csgo)
* https://twitter.com/csgolounge/status/1622899230753845248

## Delete Shader Cache

https://x.com/fREQUENCYCS/status/1841838121735856261

```bash
del /q /s "%USERPROFILE%\AppData\LocalLow\NVIDIA\PerDriverVersion\DXCache\*"
```

## Drivers

- NVIDIA GPU https://www.nvidia.com/en-us/drivers/
- AMD CPU https://www.amd.com/en/support/downloads/drivers.html/processors/ryzen/ryzen-7000-series/amd-ryzen-9-7950x3d.html