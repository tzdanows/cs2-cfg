## CS2 CFG

simplifed CS2 config setup for proficient play & practice

### 1\. CFG setup

Your config files (`.cfg`) store custom commands and settings for CS2.

**Steps:**

1.  **Clone this repository:** Get all the necessary files by cloning this GitHub repository to your computer.
2.  **Edit your config:**
    * Open `actual/config.cfg` and `actual/autoexec.cfg` with a text editor (like Notepad).
    * Modify the settings inside these files to suit your preferences (e.g., crosshair, sensitivity, keybinds).
      * *or leave them be and get used to them o7*
3.  **Match file paths in `cp.py` to the sample below:**
    * Open `cp.py` with a text editor.
    * Ensure the file paths in `cp.py` correctly point to where CS2 stores its config files on *your* computer. The default path is usually `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike 2\game\csgo\cfg\`.
   4. **Run the script:**
       * Execute `cp.py`. This script will automatically copy your customized `config.cfg` and `autoexec.cfg` into the correct CS2 folder you just set up.
       ```bash
       python3 cp.py
      ```

**To apply changes:**
After making changes to your local config files and running `cp.py`, you can either:

* Restart CS2, or
* Open the in-game console (usually `~`) and type `exec config.cfg` and press Enter.

### 2\. Launch Options

Launch options are commands that run automatically every time you start CS2 through Steam.

**How to set them:**

1.  Right-click on Counter-Strike 2 in your Steam Library.

2.  Select "Properties."

3.  At the bottom, find "Launch Options."

4.  Copy and paste the following recommended launch options:

    ```
    -novid -freq 360 -w 1280 -h 960 -tickrate 128 -fullscreen -nojoy +exec config.cfg
    ```
    or my res: `1440x1080` (may work better on 1440p monitors)
    ```
    -novid -freq 360 -w 1440 -h 1080 -tickrate 128 -fullscreen -nojoy +exec config.cfg
    ```

    * `-novid`: Skips the intro video.
    * `-freq 360`: Sets your monitor refresh rate (change `360` to your monitor's actual refresh rate).
    * `-w 1280 -h 960`: Sets your game resolution to 1280x960 (adjust as desired).
    * `-tickrate 128`: Sets the tickrate for offline servers/bots.
    * `-fullscreen`: Forces fullscreen mode.
    * `-nojoy`: Disables joystick support.
    * `+exec config.cfg`: Automatically executes your `config.cfg` file when the game starts.

### 3\. Video Settings (In-Game)

These are general recommendations for in-game video settings, often used for stretched resolutions.

* **Resolution:** 1280 x 960 stretched OR 1440 x 1080 stretched.
* For detailed video settings and what to adjust in-game, refer to this link: [Video settings here](https://github.com/tzdanows/cs2-cfg/blob/main/actual/cs2_video.txt) (potentially outdated)
* visit [the 2nd readme](https://github.com/tzdanows/cs2-cfg/blob/main/readme-2.md) for additional optimizations


---

### Contributing Guidelines:

* Contributions are welcome to the `profigs` and `playerfigs` folders to add more configurations.
* **Please make a new branch for your contributions before submitting a pull request.**
* Please **do not modify any other folders**.
* Follow the `config.cfg` naming convention within `[playername]` folders.
* Forks are always welcome for personal use.
* Overrides of pro configs are welcome, especially if they are heavily outdated.

**To checkout a new branch and make changes:**

```bash
git checkout -b <new-branch-name>
git add . ; git commit -m "cfg change" ; git push ; python .\cp.py
```