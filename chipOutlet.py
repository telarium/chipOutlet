import os
import sys
import time
import sys
import datetime

OUTLET_TOP_PIN = 118
OUTLET_BOTTOM_PIN = 120

OUTLET_TOP_HOUR_ON = 9
OUTLET_TOP_HOUR_OFF = 20

OUTLET_BOTTOM_HOUR_ON = 6
OUTLET_BOTTOM_HOUR_OFF = 22

def main(args):
	os.system( "sudo sh -c 'echo " + str(OUTLET_TOP_PIN) + " > /sys/class/gpio/export'" )
	os.system( "sudo sh -c 'echo " + str(OUTLET_BOTTOM_PIN) + " > /sys/class/gpio/export'" )

	os.system( "sudo sh -c 'echo out > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/direction'" )
	os.system( "sudo sh -c 'echo out > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/direction'" )

	bRunning = True
	currentHour = datetime.datetime.now().hour

	while( bRunning ):
		try:
			currentHour = datetime.datetime.now().hour
			if( currentHour < OUTLET_TOP_HOUR_ON or currentHour > OUTLET_TOP_HOUR_OFF ): # Should we turn outlet off?
				os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
			else:
				os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )

			if( currentHour < OUTLET_BOTTOM_HOUR_ON or currentHour > OUTLET_BOTTOM_HOUR_OFF ): # Should we turn outlet off?
                                os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )
                        else:
                                os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )
			
			time.sleep(1)
			
		except KeyboardInterrupt:
			bRunning = False

	os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
	os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )

	os.system( "sudo sh -c 'echo " + str(OUTLET_TOP_PIN) + "> /sys/class/gpio/unexport'" )
	os.system( "sudo sh -c 'echo " + str(OUTLET_BOTTOM_PIN) + "> /sys/class/gpio/unexport'" )

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
