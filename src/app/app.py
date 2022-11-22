import time
import sys

class pyapp:

    def __init__(self):
        self.on_time = 1  #in sec
        self.off_time = 3 #in sec

    def main(self):
        sys.stdout.write('\r....On' )
        sys.stdout.flush()
        time.sleep(self.on_time)
        
        sys.stdout.write('\r...Off' )
        sys.stdout.flush()
        time.sleep(self.off_time)
