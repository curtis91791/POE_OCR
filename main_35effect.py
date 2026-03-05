import pyautogui
import pytesseract
import subprocess
import time
import cv2
import numpy as np
import keyboard
import re
import os

# OCR 擷取範圍
ocr_region = (130, 190, 400, 120) 
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
pytesseract.pytesseract.tesseract_cmd = tesseract_path

#詞綴
original_targets = [
    {
        "name": "最大能量護盾",
        "pattern": r"\+(10|11|12)最大能量護盾"
    },
    {
        "name": "3%攻擊和施放速度",
        "pattern": r"混沌技能增加3%攻擊"
    },
    {
        "name": "智慧",
        "pattern": r"\+(7|8)智慧"
    },
    {
        "name": "全能力",
        "pattern": r"\+4全能力"
    },
    {
        "name": "全部抗性",
        "pattern": r"\+4%全部元素"
    }
    ]
target_keywords = original_targets.copy()


#------------AHK------------
def use_currency(name):
    subprocess.run([r"C:\Program Files\AutoHotkey\v1.1.37.02\AutoHotkeyU64.exe", os.path.join("ahk", f"{name}.ahk")])

TESSERACT_CONFIG = r'--oem 3 --psm 6'

def get_item_text():
    screenshot = pyautogui.screenshot(region=ocr_region)
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #灰階
    #gray = cv2.medianBlur(gray, 1) 
    resized_gray = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC) #放大2
    _, thresh = cv2.threshold(resized_gray, 90, 255, cv2.THRESH_BINARY_INV)
    text = pytesseract.image_to_string(thresh, lang='chi_tra',config=TESSERACT_CONFIG)

    # cv2.imshow("預覽圖", thresh)  
    # cv2.waitKey(0)  
    # cv2.destroyAllWindows()
    return text

def match_target(text):
    global target_keywords
    text_no_spaces = text.replace(" ", "")
    lines = text_no_spaces.splitlines() 
    for i, kw in enumerate(target_keywords): #移除詞綴
        if re.search(kw["pattern"], text_no_spaces):
            print(f"符合詞綴：{kw['name']}，從 target 中移除")
            target_keywords.pop(i)
            return len(target_keywords)
    return lines[-1]

#初始化
use_currency("initialization")
time.sleep(1)

while True:
    #偵測ESC被按下
    if keyboard.is_pressed('alt'):
        break
    affix_text = get_item_text()
    match_target(affix_text)
    if len(target_keywords)==2: #complete
        break
    elif len(target_keywords)==3: #崇高
        use_currency("ex")
        break
    elif len(target_keywords)==4: #富豪
        use_currency("regal")
        time.sleep(0.2)
        affix_text = get_item_text()
        match_target(affix_text)
        time.sleep(0.2)
        if len(target_keywords)==4: #重鑄
            target_keywords = original_targets.copy()
            use_currency("scouring")
            time.sleep(0.2)
            affix_text = get_item_text()
            match_target(affix_text)
    elif re.search("附加的小天賦增加35",match_target(affix_text)): #增幅
        use_currency("augment")
    else:
        use_currency("alteration")
    time.sleep(0.2)
