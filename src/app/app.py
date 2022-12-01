import os
import time

class pyapp:
    def __init__(self):
        self.ledNumber = 0
        self.on_time = 5
        self.off_time = 5
        

    def main(self):
        led = str(self.ledNumber)
        os.popen("sudo sh -c 'echo 1 > /sys/class/leds/led"+led+"/brightness'")
        time.sleep(self.on_time)
        os.popen("sudo sh -c 'echo 0 > /sys/class/leds/led"+led+"/brightness'")
        time.sleep(self.off_time)
    
    
if __name__ == "__main__":
    app = pyapp()
    app.main()
