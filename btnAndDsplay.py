import RPi.GPIO as GPIO
import time

pins = [11,12,13,15,16,18,22,7]
dats = {
	0 : 0x3f,
	1 : 0x06,
	2 : 0x5b,
	3 : 0x4f,
	4 : 0x66,
	5 : 0x6d,
	6 : 0x7d,
	7 : 0x07,
	8 : 0x7f,
	9 : 0x6f,
	10 : 0x77,
	11 : 0x7c,
	12 : 0x39,
	13 : 0x5e,
	14 : 0x79,
	15 : 0x71,
	16 : 0x80,
}
BtnPin = 40

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)   # Set pin mode as output
        GPIO.output(pin, GPIO.LOW)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def writeOneByte(num):
    val = dats[num]
    GPIO.output(11, val & (0x01 << 0))
    GPIO.output(12, val & (0x01 << 1))
    GPIO.output(13, val & (0x01 << 2))
    GPIO.output(15, val & (0x01 << 3))
    GPIO.output(16, val & (0x01 << 4))
    GPIO.output(18, val & (0x01 << 5))
    GPIO.output(22, val & (0x01 << 6))
    GPIO.output(7,  val & (0x01 << 7))

def loop(display):
    while True:
		v = GPIO.input(BtnPin)
		if v == GPIO.HIGH: # Check whether the button is pressed or not.
			writeOneByte(display)
			if display < 16:
				display += 1
			else:
				display = 0
			time.sleep(0.5)

def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop(0)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
        destroy()
