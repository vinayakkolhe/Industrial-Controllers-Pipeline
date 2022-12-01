import time
import sys
from colorama import init, Fore, Back, Style
import click
init(convert=True)


class pyapp:


    def __init__(self):
        
    
        self.on_time = 1  #in sec
        self.off_time = 1 #in sec
        self.lamp_color = "red"

    def main(self):
        """
        This is main function which is getting executed in runner in loop.
        """
        sys.stdout.write('\r....' + click.style('On', self.lamp_color))
        sys.stdout.flush()
        time.sleep(self.on_time)
        
        sys.stdout.write('\r...' + click.style('Off', self.lamp_color))
        sys.stdout.flush()
        time.sleep(self.off_time)
        
        

    
if __name__ == "__main__":
    pyapp().main()
