import pyautogui
import keyboard
import pyperclip
import time

def extract_third_value(text):
    try:
        parts = text.split('/')
        return float(parts[2]) if len(parts) >= 3 else None
    except:
        return None

def main_loop():
    while True:
        if keyboard.is_pressed("esc"):
            break

        # === Step 1: Check copiedText ===
        pyautogui.click(308, 283)
        time.sleep(0.65)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.65)
        copied_text = pyperclip.paste().strip().lower()

        if copied_text not in ['fin-0001', 'fin-0005']:
            time.sleep(7)
            continue

        # === Receipt Block ===
        pyautogui.click(1094, 236)
        time.sleep(0.55)
        pyautogui.press('down')
        time.sleep(0.45)
        pyautogui.press('tab')
        time.sleep(0.8)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.8)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.4)
        text1 = pyperclip.paste().strip()

        pyautogui.press('tab')
        time.sleep(0.4)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.4)
        text3 = pyperclip.paste().strip()

        pyautogui.press('down')
        time.sleep(0.4)
        pyautogui.press('left')
        time.sleep(0.4)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.8)
        pyautogui.write(text1)
        time.sleep(0.8)
        pyautogui.press('enter')
        time.sleep(0.45)

        # === Double click + copy for text2 ===
        pyautogui.click(1049, 259)
        pyautogui.click(1049, 259)
        pyautogui.click(1049, 259)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        text2 = pyperclip.paste().strip()

        amt1 = extract_third_value(text1)
        amt2 = extract_third_value(text2)
        if amt1 is None or amt2 is None or amt1 != amt2:
            exit()

        pyautogui.click(504, 259)
        time.sleep(0.55)

        # === Invoice Block ===
        pyautogui.click(1094, 729)
        time.sleep(0.55)
        pyautogui.press('down')
        time.sleep(0.45)
        pyautogui.press('tab')
        time.sleep(0.8)
        pyautogui.write(text3)
        time.sleep(0.7)
        pyautogui.press('enter')
        time.sleep(0.45)

        # === Double click + copy for text4 ===
        pyautogui.click(1049, 753)
        pyautogui.click(1049, 753)
        pyautogui.click(1049, 753)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        text4 = pyperclip.paste().strip()

        amt3 = extract_third_value(text3)
        amt4 = extract_third_value(text4)
        if amt3 is None or amt4 is None or amt3 != amt4:
            exit()

        pyautogui.click(503, 751)
        time.sleep(0.5)

        # === Copy value5 from 1419, 259 ===
        pyautogui.click(1419, 259)
        time.sleep(0.25)
        pyautogui.click(1419, 259)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        value5 = float(pyperclip.paste())

        # === Copy value6 from 1419, 753 ===
        pyautogui.click(1419, 753)
        time.sleep(0.25)
        pyautogui.click(1419, 753)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        value6 = float(pyperclip.paste())

        if value5 == value6:
            pyautogui.hotkey('ctrl', 's')
            time.sleep(18)
            pyautogui.click(99, 599)
            time.sleep(20)
            pyautogui.click(1159, 299)
            time.sleep(0.45)
            pyautogui.click(99, 599)
            time.sleep(4)
            pyautogui.click(99, 599)
            time.sleep(4)

            # === Copy total from 1789, 699 ===
            pyautogui.click(1789, 699)
            time.sleep(0.25)
            pyautogui.click(1789, 699)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.5)
            total = float(pyperclip.paste())
            if total < 3:
                exit()
        else:
            pyautogui.click(505, 753)
            time.sleep(0.5)
            pyautogui.click(505, 259)
            time.sleep(0.5)
            exit()

        pyperclip.copy("")
        time.sleep(0.5)

if __name__ == "__main__":
  # Click once
    time.sleep(3)        # Wait another 4 seconds
    main_loop()
