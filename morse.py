from gpiozero import LED
from time import sleep
blue = LED(17)
blue.off()

def MorseS():
    for i in range(3):
        blue.on()
        sleep(0.7)
        blue.off()
        sleep(0.7)
    blue.off()
def o():
    for i in range(3):
        blue.on()
        sleep(1.7)
        blue.off()
        sleep(1.7)
    blue.off()
# Letter S
MorseS()
# Letter O
o()
# Letter S
MorseS()

exit()
