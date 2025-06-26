# | Made by 2cz5 | https://github.com/2cz5 | Discord:2cz5 (for questions etc..)
# Modified By Windforce2007 | DBD Cake Clicker : https://github.com/windforce2007/DBD-Cake-Clicker |  https://github.com/windforce2007
import cv2
import numpy as np
import pyautogui
import threading
import time
import win32gui
import win32con
import keyboard
import os
import logging
import sys  

killswitch_activated = False

logging.basicConfig(filename='clicker.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

def minimize_cmd_window():
    try:
        hwnd = win32gui.FindWindow("ConsoleWindowClass", None)
        if hwnd != 0:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    except Exception as e:
        logging.error(f"Error minimizing command prompt window: {e}")

def monitor_killswitch(killswitch_key):
    global killswitch_activated
    while True:
        if keyboard.is_pressed('shift') and keyboard.is_pressed(killswitch_key):
            logging.info("Killswitch activated.")
            killswitch_activated = True
            break
        time.sleep(0.1)

def search_and_click(images, threshold=0.8, click_delay=0.01, killswitch_key='q'):
    method = cv2.TM_CCOEFF_NORMED
    killswitch_thread = threading.Thread(target=monitor_killswitch, args=(killswitch_key,))
    killswitch_thread.start()

    fixed_click_coords = (680, 560)  
    no_match_start_time = time.time()

    while not killswitch_activated:
        minimize_cmd_window()
        screenshot = pyautogui.screenshot()
        screen_np = np.array(screenshot)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

        match_found = False  

        for image_path in images:
            if not os.path.exists(image_path):
                logging.error(f"Image not found at '{image_path}'")
                continue

            template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            result = cv2.matchTemplate(screen_gray, template, method)
            loc = np.where(result >= threshold)

            if loc[0].size > 0:
                for pt in zip(*loc[::-1]):
                    x = pt[0] + template.shape[1] // 2
                    y = pt[1] + template.shape[0] // 2
                    pyautogui.mouseDown(x, y)
                    time.sleep(0.1)
                    pyautogui.mouseUp(x, y)
                    pyautogui.moveTo(1000, 1000)
                    logging.info(f"Clicked on {image_path} at ({x}, {y})")
                    match_found = True
                    no_match_start_time = time.time()  # ← resetujemy timer
                    time.sleep(click_delay)
                    if killswitch_activated:
                        break
            if killswitch_activated:
                break
# Modified 
        if not match_found and (time.time() - no_match_start_time >= 3):
            pyautogui.mouseDown(*fixed_click_coords)
            time.sleep(0.1)
            pyautogui.mouseUp(*fixed_click_coords)
            logging.info(f"No match found for 5 seconds. Clicked at fixed coordinates {fixed_click_coords}")
            no_match_start_time = time.time()
            time.sleep(click_delay)

        if killswitch_activated:
            break

    logging.info("Exiting the loop.")
# Modified 
def main():
    if len(sys.argv) < 2:
        print("USE: clicker.exe [--fix x,y] image1.png image2.png ...")
        print("Try Again")
        print("Example: clicker.exe --fix 680,560 image1.png")
        input("Press Enter to exit...")
        logging.error("No image paths were provided.")
        return

    fixed_click_coords = (680, 560)  # default
    image_paths = []

    for arg in sys.argv[1:]:
        if arg.startswith("--fix"):
            match = re.match(r"--fix\s*(\d+),(\d+)", arg)
            if match:
                fixed_click_coords = (int(match.group(1)), int(match.group(2)))
                logging.info(f"Using custom fixed click coordinates: {fixed_click_coords}")
            else:
                print("Invalid format for --fix. Use: --fix 680,560")
                input("Press Enter to exit...")
                return
        else:
            image_paths.append(arg)

    if not image_paths:
        print("No image paths provided.")
        input("Press Enter to exit...")
        return

    print("Working\nTo Pause Clicker Press Shift + Q")
    logging.info(f"Started with images: {image_paths} and fixed coords: {fixed_click_coords}")
    search_and_click(image_paths, fixed_click_coords=fixed_click_coords)

if __name__ == "__main__":
    main()
