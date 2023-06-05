# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 08:44:26 2022

@author: mustafa
"""

import pytesseract
import pyautogui
import pyscreeze
import time
import pyperclip
from PIL import ImageGrab
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

gidilecekYer = "Selçuklu YHT(Konya)"
bulundugunuzYer = "Eskişehir"
tarih = "04.01.2023"
neredenboxx = 1495
neredenboxy = 645

nereyeboxx = 1904
nereyeboxy = 645
while True:
    time.sleep(3)
    pyautogui.click(x=neredenboxx, y=neredenboxy)
    time.sleep(1)
    old = pyperclip.paste()
    pyperclip.copy(bulundugunuzYer)
    pyautogui.hotkey("ctrl", "v")
    pyperclip.copy(old)
    time.sleep(2)
    pyautogui.click(x=neredenboxx,y=neredenboxy+40) 
    time.sleep(1)
    pyautogui.click(x=nereyeboxx, y=nereyeboxy)
    time.sleep(1)
    old = pyperclip.paste()
    pyperclip.copy(gidilecekYer)
    pyautogui.hotkey("ctrl", "v")
    pyperclip.copy(old)
    time.sleep(2)
    pyautogui.click(x=nereyeboxx, y=nereyeboxy+40)
    time.sleep(1)
    pyautogui.click(x=1495, y=754)
    time.sleep(1)
    for i in range(25):
        pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.write(tarih)
    time.sleep(1)
    pyautogui.click(x=1599, y=1206)
    time.sleep(1)
    pyautogui.click(x=1351, y=918)
    time.sleep(5)
    image = ImageGrab.grab(bbox=(1305, 795, 1400,815))
    image.save('sc.png')
    time.sleep(2)
    try:
        #C:\Program Files\Tesseract-OCRseluklu
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        oku = pytesseract.image_to_string(r'sc.png')
        parantez = oku.find("(")
        koltuksayisi = int(oku[1])
        if koltuksayisi > 0:   
            account_sid = "AC51efada95ce35755e082da272319bc57"
            auth_token  = "79d43ca966d77cfd18ae92411efda118"
            
            client = Client(account_sid, auth_token)
            twiml = VoiceResponse()
            
            call = client.calls.create(
                from_='+13252412522',
                to='+905059400196',
                twiml=str(twiml),
            )
        else:
            pyautogui.click(x=277, y=214)
            time.sleep(1)
            pyautogui.click(x=neredenboxx, y=neredenboxy)
            time.sleep(1)
            for i in range(25):
                pyautogui.hotkey('backspace')
            time.sleep(1)
            pyautogui.click(x=1517, y=553)
            time.sleep(1)
            for i in range(25):
                pyautogui.hotkey('backspace')
    except:
        print ('Hata aldım bir sonrakine gidiyorum')
        pyautogui.click(x=277, y=214)
        time.sleep(1)
        pyautogui.click(x=neredenboxx, y=neredenboxy)
        time.sleep(1)
        for i in range(25):
            pyautogui.hotkey('backspace')
        time.sleep(1)
        pyautogui.click(x=1517, y=553)
        time.sleep(1)
        for i in range(25):
            pyautogui.hotkey('backspace')

        