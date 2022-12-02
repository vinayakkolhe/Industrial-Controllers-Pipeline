import os
import time

class pyapp:
    def __init__(self):
        self.ledNumber = 0
        self.led = str(self.ledNumber)
        self.on_time = 1
        self.off_time = 1
        os.popen("sudo sh -c 'echo none > /sys/class/leds/led0/trigger'")
        os.popen("sudo sh -c 'echo none > /sys/class/leds/led1/trigger'")
        

    def main(self):
        os.popen("sudo sh -c 'echo 1 > /sys/class/leds/led"+self.led+"/brightness'")
        time.sleep(self.on_time)
        os.popen("sudo sh -c 'echo 0 > /sys/class/leds/led"+self.led+"/brightness'")
        time.sleep(self.off_time)
    
    
if __name__ == "__main__":
    app = pyapp()
    app.main()
