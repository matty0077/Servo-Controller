
from fuchikoma2 import *
from evdev import InputDevice, list_devices, ecodes

#//////////////////joystick Check
found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    #print(dev) #to list available input devices
    if dev.name == 'Bluetooth 3.0 Macro Keyboard Keyboard':#replace with your keyboard name
        found = True;
        time.sleep(.75)
        F.move(0,77)
        time.sleep(.75)
        F.move(0,0)
        print("control system Green")
        break

if not(found):
    print('Bluetooth 3.0 Macro Keyboard not found')
    sys.exit()
##############CONTROL SYSTEM--CHANGE KEYS AND FUNCTIONS TO YOUR NEEDS
    
def handle(code):
    if code == ecodes.KEY_1:
        F.bite()
        
    if code==ecodes.KEY_H:
        F.lok()
        
    if code==ecodes.KEY_D:
        F.lopen()

    if code == ecodes.KEY_UP:
        F.shoot()
 
#//////////////////total relax sets all servos to 0
    if code == ecodes.KEY_L:
        F.servo_lax()

#////////////////////exit program
    if code == ecodes.KEY_ESC:
        sys.exit()

def Manual():
    try:
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.value == 1:  # key down(pressed)
                    handle(event.code)
                '''if event.value == 0:  # key up(released)
                    handle(event.code)'''
    except KeyboardInterrupt:
        sys.exit()

Manual()
