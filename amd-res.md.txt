# 9070 XT CS2 res fix

troubleshooting steps to fix resolution issues for a 9070 XT AMD graphics card in CS2

## fullscreen crash upon resolution swap

1. go to steam & right click CS2 properties --> installed files --> browse (your entrypoint for cs2 files)
2. navigate through these folders: game --> --> bin --> win64
3. in win64, find the cs2 / cs2.exe file and go to properties
4. go to the compatibility tab and check "disable fullscreen optimizations"

this has temporarily fixed my issues of the game crashing upon changing my resolution to 4:3 variants ingame

## resolution swaps in AMD's adrenaline

1. open adrenaline, go to the gaming tab, select cs2
2. scroll down and click on global display (or just cs2, but I had to do global)
3. create new custom resolution, insert these values depending on your resolution and hz (mine was 360hz)


### 1080x960

```json
{
  "Resolution": {
    "Horizontal": 1080,
    "Vertical": 960
  },
  "RefreshRateHz": 359,
  "Presentation": "Progressive",
  "TimingStandard": "Manual",
  "GPixelClock_kHz": 526880,
  "GRefreshRate_Hz": 358.996,
  "TimingInfo": {
    "Total": {
      "Horizontal": 1176,
      "Vertical": 1248
    },
    "Display": {
      "Horizontal": 1080,
      "Vertical": 960
    },
    "FrontPorch": {
      "Horizontal": 32,
      "Vertical": 3
    },
    "SyncWidth": {
      "Horizontal": 32,
      "Vertical": 5
    }
  },
  "TimingPolarity": {
    "Horizontal": "Positive",
    "Vertical": "Negative"
  }
}
```

### 1440x1080

```json
{
  "Resolution": {
    "Horizontal": 1440,
    "Vertical": 1080
  },
  "RefreshRateHz": 359,
  "Presentation": "Progressive",
  "TimingStandard": "Manual",
  "GPixelClock_kHz": 702720,
  "GRefreshRate_Hz": 358.996,
  "TimingInfo": {
    "Total": {
      "Horizontal": 1608,
      "Vertical": 1248
    },
    "Display": {
      "Horizontal": 1440,
      "Vertical": 1080
    },
    "FrontPorch": {
      "Horizontal": 32,
      "Vertical": 3
    },
    "SyncWidth": {
      "Horizontal": 32,
      "Vertical": 5
    }
  },
  "TimingPolarity": {
    "Horizontal": "Positive",
    "Vertical": "N

```


### 1920x1080

should be default, but the g.pixel kHz I had was 967680 & timing front porch 48/3 (horiz/vert)

