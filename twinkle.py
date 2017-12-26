#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BZRPin = 12

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)

#Dictionary for notes

notes = {
	'C3': 130.81,
	'D3': 146.83,
	'E3': 164.81,
	'F3': 174.61,
	'G3': 196.00,
	'A3': 220.00,
	'B3': 246.94,
	'C4': 261.63,
	'D4': 293.66,
	'E4': 329.63,
	'F4': 349.23,
	'G4': 392.00,
	'A4': 440.00,
	'B4': 493.88,
}

TWINKLE_1 = 'C4,,C4,,G4,,G4,,A4,,A4,,G4,G4,G4,'

TWINKLE_2 = 'F4,,F4,,E4,,E4,,D4,,D4,,C4,C4,C4,'

TWINKLE_3 = 'G3,,G3,,F3,,F3,,E3,,E3,,D3,D3,D3,'

TWINKLE = ','.join([TWINKLE_1, TWINKLE_2, TWINKLE_3, TWINKLE_3, TWINKLE_1, TWINKLE_2])

#DOADEER = 'CDECECE' Forget this

SLEEP_TIME = 0.25

def main():
	p = GPIO.PWM(BZRPin, 50) # init frequency: 50HZ

	try:
		started = False
		for note in TWINKLE.split(","):
			if note.strip() == '':
				if started:
					started = False
					p.stop()
				time.sleep(SLEEP_TIME)
				continue

			f = notes.get(note)
			p.ChangeFrequency(f)
			if not started:
				started = True
				p.start(50)
			time.sleep(SLEEP_TIME)
	except KeyboardInterrupt:
		pass
	finally:
		p.stop()
		GPIO.cleanup()

if __name__ == "__main__":
	main()

