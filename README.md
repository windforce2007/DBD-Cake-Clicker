# DBD Bloodweb Cake Clicker  
**Version 1.0 by [Windforce2007](https://www.twitch.tv/windforce2007)**  
*Based on the original by [2cz5](https://github.com/2cz5)*


## ▶ DESCRIPTION

An automated image-based clicker for Dead by Daylight's Bloodweb,  
designed to automatically click cakes to collect as many as possible.

Works best on **1920x1080** resolution.

If you're using a different screen size, you can provide a fallback click position using the `--fix` argument:

**`--fix x,y`** — where `x,y` are the coordinates of the Automatic Purchase button.

## ▶ USAGE

1. Place your target image(s) in the same folder as the `.exe`
2. Open a command prompt
3. Run it like this:

```bash
Image-Clicker.exe [--fix x,y] image1.png image2.png
```
▶ EXAMPLES:

- Default (1920x1080):
```bash
   Image-Clicker.exe Cake.png
```
- Custom fallback click location (e.g. 680,560):
```bash
   Image-Clicker.exe --fix 680,560 Cake.png
```
▶ CONTROLS:

- Pause/Exit the clicker anytime with:
  
      SHIFT + Q

▶ REQUIREMENTS:

- Windows OS
- 1920x1080 display (or use --fix)
- Images of the clickable target (cakes, etc.)

▶ LICENSE:

This project is based on work by 2cz5  
GitHub: https://github.com/2cz5  
Licensed under the GNU General Public License v3.0  
Modifications by Windforce2007

