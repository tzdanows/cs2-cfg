## CS2 CFG

simplifed CS2 config setup for proficient play & practice

### 1\. CFG setup

Your config files (`.cfg`) store custom commands and settings for CS2.

**Steps:**

1.  **Clone this repository.**
2.  **Edit your config:** open `actual/config.cfg` and `actual/autoexec.cfg` in a text editor and adjust to taste (crosshair, sensitivity, keybinds) — *or leave them as-is o7*.
3.  **Set your CS2 cfg path in `cp.py`:** default is `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike 2\game\csgo\cfg\`.
4.  **Run it:**
    ```bash
    python3 cp.py
    ```

**To apply changes:**
After making changes to your local config files and running `cp.py`, you can either:

* Restart CS2(launch options or autoexec will apply), or
* Open the in-game console (usually `~`) and type `exec settings` and press Enter.

### 2\. Launch Options

Launch options are commands that run automatically every time you start CS2 through Steam.

**How to set them:**

1.  Right-click on Counter-Strike 2 in your Steam Library.

2.  Select "Properties."

3.  At the bottom, find "Launch Options."

4.  Copy and paste the following recommended launch options:

    ```
    -novid -freq 360 -w 1280 -h 960 -tickrate 128 -fullscreen -nojoy +exec settings.cfg
    ```
    or my res: `1440x1080` (may work better on 1440p monitors)
    ```
    -novid -freq 360 -w 1440 -h 1080 -tickrate 128 -fullscreen -nojoy +exec config.cfg
    ```

    | Flag | Effect |
    |---|---|
    | `-novid` | Skip intro video |
    | `-freq 360` | Monitor refresh rate (match yours) |
    | `-w`/`-h` | Game resolution |
    | `-tickrate 128` | Tickrate for offline servers/bots |
    | `-fullscreen` | Force fullscreen |
    | `-nojoy` | Disable joystick support |
    | `+exec <file>.cfg` | Config to run on launch |

### 3\. Video Settings (In-Game)

These are general recommendations for in-game video settings, often used for stretched resolutions.

* **Resolution:** 1280 x 960 stretched OR 1440 x 1080 stretched.
* Reference: [`actual/cs2_video.txt`](https://github.com/tzdanows/cs2-cfg/blob/main/actual/cs2_video.txt) (potentially outdated)
* See [`docs/OPTIMIZATIONS.md`](https://github.com/tzdanows/cs2-cfg/blob/main/docs/OPTIMIZATIONS.md) for further tuning


---

### Contributing Guidelines:

* Contributions are welcome to the `playerfigs` folder to add more configurations.
* **Please make a new branch for your contributions before submitting a pull request.**
* Please **do not modify any other folders**.
* Follow the `config.cfg` naming convention within `[playername]` folders.
* Forks are always welcome for personal use.

**To checkout a new branch and make changes:**

```bash
git checkout -b <new-branch-name>
git add . ; git commit -m "cfg change" ; git push ; python .\cp.py
```

**video settings location: + update 2/16/2026 --> **
```bash
C:\Program Files (x86)\Steam\userdata\115874183\730\local\cfg
```
```json
amd-anti-lag: off
amd-free-sync: off
scaling-mode: full panel
```
