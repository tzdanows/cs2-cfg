## Optimizations:

additional optimizations I tend to consider

### 1\. NVIDIA Control Panel

* **Digital Vibrance:** 80%, or 50% default.
* **3D Settings:** [example config](https://i.imgur.com/vs5EpQx.gif). Commonly tweaked:
  * `Texture Filtering - Quality`: High Performance
  * `Threaded Optimization`: On
  * `Low Latency Mode`: Ultra (lowest input lag, if available)
  * `Shader Cache Size`: Driver Default, or 10GB+ to reduce stuttering
  * `V-Sync`: Off
* **Resolution:** select your monitor's native res/highest refresh rate (e.g. 1920x1080 @ 360Hz). A stretched res (e.g. 1280x960) just needs to exist in the panel, not be selected.
* **Desktop Scaling:** "Full-Screen" mode to avoid black bars on stretched resolutions.

### 2\. Hypervisor toggle

Can interfere with performance or anti-cheat, depending on the game. Run as Administrator:

```bash
bcdedit /set hypervisorlaunchtype auto   # enable (some anti-cheats want this)
bcdedit /set hypervisorlaunchtype off    # disable (if you hit issues)
```

### 3\. Clear shader cache

Fixes stuttering/glitches after driver or game updates.

1. Close CS2 and Steam.
2. Delete contents of `%USERPROFILE%\AppData\LocalLow\NVIDIA\PerDriverVersion\DXCache\` (and `...\AppData\Local\NVIDIA\DXCache\` if present).
3. Delete contents (not the folder) of `C:\Program Files (x86)\Steam\steamapps\shadercache\730`.
4. Optional: verify game file integrity in Steam.
5. Restart.

### 4\. Update drivers

* [NVIDIA GPU drivers](https://www.nvidia.com/en-us/drivers/)
* [AMD CPU drivers](https://www.amd.com/en/support/downloads/drivers.html) (select your CPU model)

### 5\. Further reading

* **modern cs2 optimization:** [https://refrag.gg/blog/the-ultimate-cs2-optimization-guide/](https://refrag.gg/blog/the-ultimate-cs2-optimization-guide/)
* **old csgo pc optimization:** [https://wiki.refrag.gg/en/pc-optimization-increase-fps-csgo](https://wiki.refrag.gg/en/pc-optimization-increase-fps-csgo)
* **old optimization tips:** [https://twitter.com/csgolounge/status/1622899230753845248](https://twitter.com/csgolounge/status/1622899230753845248)
* pro-cfg-list
  * **donk cfg:** [donk-cfg](https://prosettings.net/players/donk/)
  * **kyousuke cfg:** [kyousuke-cfg](https://prosettings.net/players/kyousuke/)
  * **stewie2k cfg:** [stew2k-cfg](https://prosettings.net/players/stewie2k/)
  * **s1mple cfg:** [s1mple-cfg](https://prosettings.net/players/s1mple/)
  * **niko cfg:** [niko-cfg](https://prosettings.net/players/niko/)
  * **ropz cfg:** [ropz-cfg](https://prosettings.net/players/ropz/)
  * **zywoo cfg:** [zywoo-cfg](https://prosettings.net/players/zywoo/)
  * **austin cfg:** [austin-cfg](https://prosettings.net/players/austin/) (just cuz 1440x1080)
  * **electronic cfg:** [electronic-cfg](https://prosettings.net/players/electronic/) (more 1440x1080)
