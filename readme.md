# CSGO config
1. Clone this repository
2. Edit files in the "actual" folder to match your preferred settings
3. Match your config filepaths with the defaults associated to the game(s)
4. Execute cp.py and it should copy/paste your cfg into the corresponding folders

# NVIDIA Control Panel
* Digital Vibrance: 80% or 50%(default)
* [3D Settings](https://i.imgur.com/vs5EpQx.gif) (potentially not optimal)
* Change Resolution --> 1920x1080(native) @ 360hz
	* Customize Resolution to make 1440x1080 resolution but keep native (will enable ingame option for 1440x1080)
* Adjust Desktop Size and Position --> Full-Screen
# Launch Options 

### CSGO: 
```
-console -novid -freq 360 -w 1440 -h 1080 -tickrate 128 +fps_max 999 +rate 786432 +exec config.cfg +exec autoexec.cfg 
```

### CS2: 

```
-console -novid -freq 360 -w 1440 -h 1080 -tickrate 128 +fps_max 999 +rate 786432 +exec cs2.cfg +exec autoexec.cfg
```
or can you exec ingame with `exec config` or `exec cs2` in console(may need .cfg after filename)
# Follow these configuration tips:

* [https://wiki.refrag.gg/en/pc-optimization-increase-fps-csgo](https://wiki.refrag.gg/en/pc-optimization-increase-fps-csgo)
* https://twitter.com/csgolounge/status/1622899230753845248
* Use per key binding for utility (Examples: C,V,F,G)

# Extras 
### Enable Hypervisor 
```
bcdedit /set hypervisorlaunchtype auto  
```

### Disable Hypervisor  
```
bcdedit /set hypervisorlaunchtype off  
```
Frequent faceit necessary toggle

### Leetify clanid

leetify "cl_clanid" `36953142`

# Video Settings:

Resolution: 1440 x 1080 stretched or preferred resolution

- Global Shadow Quality: HIGH
- Model / Texture Detial: LOW
- Texture Streaming: DISABLED
- Effect Detail: HIGH
- Shader Detail: VERY HIGH
- Boost Player Contrast: ENABLED
- Multicore Rendering: ENABLED (mat_queue_mode 2)
- MSAA: None
- FXAA: Disabled
- Texture Filtering: Trilinear
- VSYNC: off
- blur: off
- uber shaders: ENABLED
