import os
import sys
import time
import sys
import datetime
import random

OUTLET_TOP_PIN = 118
OUTLET_BOTTOM_PIN = 120

def main(args):
	os.system( "sudo sh -c 'echo " + str(OUTLET_TOP_PIN) + " > /sys/class/gpio/export'" )
	os.system( "sudo sh -c 'echo " + str(OUTLET_BOTTOM_PIN) + " > /sys/class/gpio/export'" )

	os.system( "sudo sh -c 'echo out > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/direction'" )
	os.system( "sudo sh -c 'echo out > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/direction'" )

	bRunning = True

	while( bRunning ):
		try:
			time.sleep(1)
			print("Turn top and bottom off")
			os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
			os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )
			time.sleep( random.randint(10,30) )
			print("Turn top and bottom on")
			os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
			os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )
	
			time.sleep(20)
			os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
			time.sleep( random.randint(10,30) )
			os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )			

			time.sleep(10)
			os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )
			time.sleep( random.randint(10,30) )
			os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )

			time.sleep(30)
			os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
                        time.sleep( random.randint(10,30) )
                        os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )

			time.sleep(5)
			os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )
                        time.sleep( random.randint(10,30) )
                        os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )

			time.sleep(45)
                        os.system( "sudo sh -c 'echo 1 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
                        time.sleep( random.randint(10,30) )
                        os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
			
		except KeyboardInterrupt:
			bRunning = False

	os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_TOP_PIN) + "/value'" )
	os.system( "sudo sh -c 'echo 0 > /sys/class/gpio/gpio" + str(OUTLET_BOTTOM_PIN) + "/value'" )

	os.system( "sudo sh -c 'echo " + str(OUTLET_TOP_PIN) + "> /sys/class/gpio/unexport'" )
	os.system( "sudo sh -c 'echo " + str(OUTLET_BOTTOM_PIN) + "> /sys/class/gpio/unexport'" )

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
