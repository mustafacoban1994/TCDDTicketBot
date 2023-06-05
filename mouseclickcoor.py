import pyautogui
import pyscreeze
import time

y = [664,732,832]
x = [1088,1008,942,858,813]
sayi = 0
while True:
    print (pyautogui.position())
    coor = pyautogui.position(x = 1007, y = 961)
    screen=pyscreeze.screenshot()
    rgb_values=screen.getpixel((coor))
    print (rgb_values)
    '''
    for i in range(len(x)):
        for j in range(len(y)):
            pyautogui.moveTo(x[0], y[0])
            pyautogui.dragTo(x[i], y[0], 0.1)
            pyautogui.dragTo(x[i], y[1], 0.1)
            pyautogui.dragTo(x[i], y[2], 0.1)
    
    #x0 x1 oluyor y0 da devam ediyor
    pyautogui.click(1008, 664)
    time.sleep(1)
    #pyautogui.moveTo(1008, 664)
    #time.sleep(1)
    pyautogui.dragTo(858, 664,2, button='left')
    time.sleep(1)
    
    pyautogui.moveTo(1088, 664)
    pyautogui.dragTo(942, 664)
    
    pyautogui.moveTo(1088, 664)
    pyautogui.dragTo(858, 664)
    
    pyautogui.moveTo(1088, 664)
    pyautogui.dragTo(813, 664)
    '''
    
    
    '''
    pyautogui.moveTo(1088, 664)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1008, 664, 1)
    time.sleep(10)
    '''
    '''
    if rgb_values == (40,118,239):
        pyautogui.click(x=1019, y=956)
        time.sleep(1)   
        pyautogui.click(x=1019, y=956)
        time.sleep(1)
        #ana ekranda ayarlara tikladi
        pyautogui.click(x=1181, y=121)
        time.sleep(1)
    #1019 956 devam koordinatı
        #arkadaslara tikladi
        pyautogui.click(x=1078, y=208)
        time.sleep(1)
        #ortak savas gir
        pyautogui.click(x=1100, y=833)
        time.sleep(1)
        pyautogui.click(x=812, y=541)
    #1019 956 devam koordinatı
        #arkadaslara tikladi
        pyautogui.click(x=1078, y=208)
    #devam renk (38, 113, 230)
    '''
    
    
    '''
    1088 664
while True:
    pyautogui.moveTo(1088, 664)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1008, 664, 1)
    time.sleep(10)
    
    1008 664
    942  664
    858  664
    813  664
         732
         832
    '''