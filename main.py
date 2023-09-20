import pyautogui as pag
import keyboard

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

def tankbuild():
    # каркас ебучий
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
    # колеса даунские
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
    # колеса даунские
    pag.mouseDown()
    pag.mouseUp()
    pag.moveTo(wheel1)
    pag.mouseDown()
    pag.mouseUp()
    pag.moveTo(wheel2)
    pag.mouseDown()
    pag.mouseUp()
    # контролер блядский
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
    # двигатель ебаный
    pag.moveRel(-130,-150)
    engine=(pag.position())
    keyboard.press('q')
    pag.moveTo(enginetab)
    pag.mouseDown()
    pag.mouseUp()
    keyboard.release('q')
    pag.moveTo(engine)
    pag.mouseDown()
    pag.mouseUp()
    # каробка ебаная
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

keyboard.add_hotkey('Alt + 1', tankbuild)


keyboard.wait('Ctrl + Q')


