import pyautogui as pag
import keyboard
from tkinter import *


tankselected = 0

root = Tk()
root.title('autotank 0')
root.geometry('500x600')
root.resizable(width=False, height=False)
root.iconbitmap('autotank.ico')

tank1image = PhotoImage(file="tank1.png")
tank2image = PhotoImage(file="tank2.png")

label1 = Label(root, text=("танг выбраный:",tankselected), font=40)
label1.pack(side=BOTTOM)

label2 = Label(root, text=("чтобы начать процесс самоуничтожения системы нажмите alt + 1"), font=1)
label2.pack(side=BOTTOM)


pag.FAILSAFE = False
timepause = 0.20
timepause3 = 0.5
timepause2 = 0.2

wheel1 = float
wheel2 = float
engine = float
control = float
gearbox = float
cannon = float


smallwheel = (944,980)
vehiclecontrol = (1250,80)
enginetab = (1350,80)
gearboxtab = (1450,80)
devicestab = (744,1040)

print ("автотанк запущен ")

def tank1buttonclick():
    global tankselected
    print("я даун")
    tankselected=1
    label1.config(text= ("танг выбраный:",tankselected))

def tank2buttonclick():
    global tankselected
    print("я даун 2")
    tankselected=2
    label1.config(text= ("танг выбраный:",tankselected))

def tankbuild():
    if tankselected == 1:
        # каркас
        pag.dragRel(0,-200, timepause, button='left')
        pag.PAUSE = timepause2
        pag.moveRel(0,90, timepause)
        pag.PAUSE = timepause2
        pag.dragRel(0,-200, timepause, button='left')
        pag.PAUSE = timepause2
        pag.moveRel(90,150, timepause)
        pag.dragRel(140,0, timepause3)
        pag.PAUSE = timepause2
        pag.moveRel(-310,0, timepause)
        pag.dragRel(-145,0, timepause3)
        pag.PAUSE = timepause2
        # колеса
        pag.moveRel(110,40, timepause2)
        wheel1=(pag.position()) 
        pag.PAUSE = timepause2
        pag.moveRel(240,0, timepause2)
        wheel2=(pag.position())
        print (wheel1,wheel2)
        pag.moveTo(devicestab)
        pag.mouseDown()
        pag.mouseUp()
        pag.moveTo(smallwheel)
        # колеса
        pag.mouseDown()
        pag.mouseUp()
        pag.moveTo(wheel1)
        pag.mouseDown()
        pag.mouseUp()
        pag.moveTo(wheel2)
        pag.mouseDown()
        pag.mouseUp()
        # контролер
        pag.moveRel(-120,-15)
        control=(pag.position())
        pag.PAUSE = timepause2
        pag.moveTo(devicestab)
        pag.mouseDown()
        pag.mouseUp()
        keyboard.press('q')
        pag.moveTo(vehiclecontrol)
        pag.mouseDown()
        pag.mouseUp()
        keyboard.release('q')
        pag.moveTo(control)
        pag.mouseDown()
        pag.mouseUp()
        # двигатель
        pag.moveRel(-130,-110)
        engine=(pag.position())
        keyboard.press('q')
        pag.moveTo(enginetab)
        pag.mouseDown()
        pag.mouseUp()
        keyboard.release('q')
        pag.moveTo(engine)
        pag.mouseDown()
        pag.mouseUp()
        # каробка
        pag.moveRel(150,0)
        gearbox=(pag.position())
        keyboard.press('q')
        pag.moveTo(gearboxtab)
        pag.mouseDown()
        pag.mouseUp()
        keyboard.release('q')
        pag.moveTo(gearbox)
        pag.mouseDown()
        pag.mouseUp()
    if tankselected == 2:
        pag.dragRel(0,-200, timepause, button='left')
        pag.PAUSE = timepause2
        pag.moveRel(0,90, timepause)
        pag.PAUSE = timepause2
        pag.dragRel(0,-200, timepause, button='left')
        pag.PAUSE = timepause2
        pag.moveRel(90,150, timepause)
        pag.dragRel(140,0, timepause3)
        pag.PAUSE = timepause2
        pag.moveRel(-310,0, timepause)
        pag.dragRel(-145,0, timepause3)
        pag.PAUSE = timepause2



tank1button = Button(root, text="танг адин", font=50, command=tank1buttonclick, image=tank1image)
tank1button.pack()

tank2button = Button(root, text="танг дыва", font=50, command=tank2buttonclick, image=tank2image)
tank2button.pack()

keyboard.add_hotkey('Alt + 1', tankbuild)


root.mainloop()





#keyboard.wait('Ctrl + Q')


