from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import time
import sys


# parser = argparse.ArgumentParser()
# parser.add_argument("x", help="the x value of the click", type=int)
# parser.add_argument("y", help="the y value of the click", type=int)
# args = parser.parse_args()

# if args.x and args.y:
#     device = MonkeyRunner.waitForConnection()
#     device.touche(x, y, MonkeyDevice.DOWN_AND_UP)
#     img = device.takeSnapshot()
#     img.writeToFile("/Users/MacBook/offlineDesktop/python/HarambeRunner/actual.png", 'PNG')
def main():
	if len(sys.argv) == 3:
		x =  int(sys.argv[1])
		y =  int(sys.argv[2])

		device = MonkeyRunner.waitForConnection()
		device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
		time.sleep(1)
		img = device.takeSnapshot()
		img.writeToFile("/Users/MacBook/offlineDesktop/python/HarambeRunner/actual.png", 'PNG')
		return "salam"

main()